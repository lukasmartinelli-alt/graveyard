"""
fs.contrib.dropboxfs
========

A FS object that integrates with Dropbox.

"""

import time
import stat
import shutil
import optparse
import datetime
import tempfile
import os.path

from fs.base import *
from fs.path import *
from fs.errors import *
from fs.filelike import StringIO

from dropbox import rest
from dropbox import client
from dropbox import session


# Items in cache are considered expired after 5 minutes.
CACHE_TTL = 300
# The format Dropbox uses for times.
TIME_FORMAT = '%a, %d %b %Y %H:%M:%S +0000'

class ContextManagerStream(object):
    def __init__(self, temp):
        self.temp = temp

    def __iter__(self):
        while True:
            data = self.read(16384)
            if not data:
                break
            yield data

    def __getattr__(self, name):
        return getattr(self.temp, name)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class SpooledWriter(ContextManagerStream):
    """Spools bytes to a StringIO buffer until it reaches max_buffer. At that
    point it switches to a temporary file."""
    def __init__(self, client, path, max_buffer=1024**2):
        self.client = client
        self.path = path
        self.max_buffer = max_buffer
        self.bytes = 0
        super(SpooledWriter, self).__init__(StringIO())

    def __len__(self):
        return self.bytes

    def write(self, data):
        if self.temp.tell() + len(data) >= self.max_buffer:
            temp = tempfile.TemporaryFile()
            temp.write(self.temp.getvalue())
            self.temp = temp
        self.temp.write(data)
        self.bytes += len(data)

    def close(self):
        # Need to flush temporary file (but not StringIO).
        if hasattr(self.temp, 'flush'):
            self.temp.flush()
        self.temp.seek(0)
        self.client.put_file(self.path, self, overwrite=True)
        self.temp.close()


class CacheItem(object):
    """Represents a path in the cache. There are two components to a path.
    It's individual metadata, and the children contained within it."""
    def __init__(self, metadata=None, children=None, timestamp=None):
        self.metadata = metadata
        self.children = children
        if timestamp is None:
            timestamp = time.time()
        self.timestamp = timestamp

    def _get_expired(self):
        if self.timestamp <= time.time() - CACHE_TTL:
            return True
    expired = property(_get_expired)

    def renew(self):
        self.timestamp = time.time()


class DropboxClient(client.DropboxClient):
    """A wrapper around the official DropboxClient. This wrapper performs
    caching as well as converting errors to fs exceptions."""
    def __init__(self, *args, **kwargs):
        super(DropboxCache, self).__init__(*args, **kwargs)
        self.cache = {}

    def clear_cache(self):
        self.cache.clear()

    # Below we split the DropboxClient metadata() method into two methods
    # metadata() and children(). This allows for more fine-grained fetches
    # and caching.

    def metadata(self, path):
        "Gets metadata for a given path."
        item = self.cache.get(path)
        if not item or item.metadata is None or item.expired:
            metadata = super(DropboxCache, self).metadata(path, list=False)
            item = self.cache[path] = CacheItem(metadata)
        # Copy the info so the caller cannot affect our cache.
        return dict(item.metadata.items())

    def children(self, path):
        "Gets children of a given path."
        item = self.cache.get(path)
        if not item or item.children is None or item.expired:
            # We might have up-to-date metadata for this path.
            if not item.expired and item.metadata:
                # in that case, if the metadata indicates that the
                # path is not a directory, we should refuse to try
                # to list it.
                if item.metadata.get('is_dir'):
                    # TODO: find the proper fs Exception to raise here.
                    raise ResourceInvalidError(path)
            hash = None
            # Use the hash to detect unchanged listings (if available).
            if not item.children is None and not item.metadata is None:
                hash = item.metadata['hash']
            try:
                metadata = super(DropboxCache, self).metadata(path, hash=hash, list=True)
            except rest.ErrorResponse, e:
                if not item or e.status != 304:
                    raise
                # We have an item from cache (perhaps expired), but it's
                # hash is still valid (as far as Dropbox is concerned),
                # so just renew it and keep using it.
                item.renew()
            children = []
            contents = metadata.pop('contents')
            for child in contents:
                name = child['name']
                children.append(name)
                self.cache[pathjoin(path, name)] = CacheItem(child)
            item = self.cache[path] = CacheItem(metadata, children)
        return item.children

    def file_create_folder(self, path):
        "Add newly created directory to cache."
        try:
            metadata = super(DropboxCache, self).file_create_folder(path)
        except rest.ErrorResponse, e:
            if e.status == 404:
                raise ParentDirectoryMissingError(path)
            if e.status == 403:
                raise DestinationExistsError(path)
            raise
        self.cache[path] = CacheItem(metadata)

    def file_copy(self, src, dst):
        try:
            metadata = super(DropboxCache, self).file_copy(src, dst)
        except rest.ErrorResponse, e:
            if e.status == 404:
                raise ResourceNotFoundError(src)
            if e.status == 403:
                raise DestinationExistsError(dst)
            raise
        self.cache[dst] = CacheItem(metadata)

    def file_move(self, src, dst):
        try:
            metadata = super(DropboxCache, self).file_move(src, dst)
        except rest.ErrorResponse, e:
            if e.status == 404:
                raise ResourceNotFoundError(src)
            if e.status == 403:
                raise DestinationExistsError(dst)
            raise
        self.cache[dst] = CacheItem(metadata)
        self.cache.pop(src, None)

    def file_delete(self, path):
        try:
            super(DropboxCache, self).file_delete(path)
        except rest.ErrorResponse, e:
            if e.status == 404:
                raise ResourceNotFoundError(path)
            raise
        self.cache.pop(path, None)

    def put_file(self, path, f, overwrite=False):
        metadata = super(DropboxCache, self).put_file(path, f, overwrite=overwrite)
        self.cache[path] = CacheItem(metadata)


def create_client(app_key, app_secret, access_type, token_key, token_secret):
    """Uses token from create_token() to gain access to the API."""
    s = session.DropboxSession(app_key, app_secret, access_type)
    s.set_token(token_key, token_secret)
    return DropboxClient(s)


def metadata_to_info(metadata):
    isdir = metadata.get('is_dir', false)
    info = {
        'size': metadata.get('bytes', 0),
        'isdir': isdir,
        'isfile': not isdir,
    }
    try:
        mtime = metadata['modified']
        mtime = time.strptime(mtime, TIME_FORMAT)
        info['modified_time'] = datetime.datetime.fromtimestamp(mtime)
    except KeyError:
        pass
    return info


class DropboxFS(FS):
    """A FileSystem that stores data in Dropbox."""

    _meta = { 'thread_safe' : True,
              'virtual' : False,
              'read_only' : False,
              'unicode_paths' : True,
              'case_insensitive_paths' : True,
              'network' : True,
              'atomic.setcontents' : False,
              'atomic.makedir': True,
              'atomic.rename': True,
              'mime_type': 'virtual/dropbox',
             }

    def __init__(self, app_key, app_secret, access_type, token_key, token_secret, thread_synchronize=True):
        """Create an fs that interacts with Dropbox.

        :param app_key: Your app key assigned by Dropbox.
        :param app_secret: Your app secret assigned by Dropbox.
        :param access_type: Type of access requested, 'dropbox' or 'app_folder'.
        :param token_key: The oAuth key you received after authorization.
        :param token_secret: The oAuth secret you received after authorization.
        :param thread_synchronize: set to True (default) to enable thread-safety
        """
        super(DropboxFS, self).__init__(thread_synchronize=thread_synchronize)
        self.client = create_client(app_key, app_secret, access_type, token_key, token_secret)

    def __str__(self):
        return "<DropboxFS: >"

    def __unicode__(self):
        return u"<DropboxFS: >"

    def getmeta(self, meta_name, default=NoDefaultMeta):
        
        if meta_name == 'read_only':
            return self.read_only
        return super(DropboxFS, self).getmeta(meta_name, default)

    @synchronize
    def open(self, path, mode="rb", **kwargs):
        if 'r' in mode:
            return ContextManagerStream(self.client.get_file(path))
        else:
            return SpooledWriter(self.client, path)

    @synchronize
    def getcontents(self, path, mode="rb"):
        path = abspath(normpath(path))
        return self.open(self, path, mode).read()

    def setcontents(self, path, data, *args, **kwargs):
        path = abspath(normpath(path))
        self.client.put_file(path, data, overwrite=True)

    def desc(self, path):
        return "%s in Dropbox" % path

    def getsyspath(self, path, allow_none=False):
        "Returns a path as the Dropbox API specifies."
        path = abspath(normpath(path))
        return client.format_path(path)

    def isdir(self, path):
        try:
            info = self.getinfo(path)
            return info.get('isdir', False)
        except ResourceNotFoundError:
            return False

    def isfile(self, path):
        try:
            info = self.getinfo(path)
            return not info.get('isdir', False)
        except ResourceNotFoundError:
            return False

    def exists(self, path):
        try:
            self.getinfo(path)
            return True
        except ResourceNotFoundError:
            return False

    def listdir(self, path="/", wildcard=None, full=False, absolute=False, dirs_only=False, files_only=False):
        path = abspath(normpath(path))
        try:
            children = self.client.children(path)
        except rest.ErrorResponse, e:
            if e.status == 404:
                raise ResourceNotFoundError(path)
            raise
        return self._listdir_helper(path, children, wildcard, full, absolute, dirs_only, files_only)

    @synchronize
    def getinfo(self, path):
        path = abspath(normpath(path))
        try:
            metadata = self.client.metadata(path)
        except rest.ErrorResponse, e:
            if e.status == 404:
                raise ResourceNotFoundError(path)
            raise
        return metadata_to_info(metadata)

    def copy(self, src, dst, *args, **kwargs):
        src = abspath(normpath(src))
        dst = abspath(normpath(dst))
        self.client.file_copy(src, dst)

    def copydir(self, src, dst, *args, **kwargs):
        src = abspath(normpath(src))
        dst = abspath(normpath(dst))
        self.client.file_copy(src, dst)

    def move(self, src, dst, *args, **kwargs):
        src = abspath(normpath(src))
        dst = abspath(normpath(dst))
        self.client.file_move(src, dst)

    def movedir(self, src, dst, *args, **kwargs):
        src = abspath(normpath(src))
        dst = abspath(normpath(dst))
        self.client.file_move(src, dst)

    def rename(self, src, dst, *args, **kwargs):
        src = abspath(normpath(src))
        dst = abspath(normpath(dst))
        try:
            self.client.file_move(src, dst)
        except rest.ErrorResponse, e:
            if e.status == 404:
                raise ResourceNotFoundError(src)
            raise

    def makedir(self, path, recursive=False, allow_recreate=False):
        path = abspath(normpath(path))
        try:
            self.client.file_create_folder(path)
        except FSError:
            # The DropboxClient already handles some fs specific error
            # conditions.
            raise
        except Exception, e:
            # Other ones depend on the caller...
            raise OperationFailedError('makedir')

    # This does not work, httplib refuses to send a Content-Length: 0 header
    # even though the header is required. We can't make a 0-length file.
    #def createfile(self, path, wipe=False):
    #    self.client.put_file(path, '', overwrite=False)

    def remove(self, path):
        path = abspath(normpath(path))
        self.client.file_delete(path)

    def removedir(self, path, *args, **kwargs):
        path = abspath(normpath(path))
        self.client.file_delete(path)


def main():
    parser = optparse.OptionParser(prog="dropboxfs", description="CLI harness for DropboxFS.")
    parser.add_option("-k", "--app-key", help="Your Dropbox app key.")
    parser.add_option("-s", "--app-secret", help="Your Dropbox app secret.")
    parser.add_option("-t", "--type", default='dropbox', choices=('dropbox', 'app_folder'), help="Your Dropbox app access type.")
    parser.add_option("-a", "--token-key", help="Your access token key (if you previously obtained one.")
    parser.add_option("-b", "--token-secret", help="Your access token secret (if you previously obtained one.")

    (options, args) = parser.parse_args()

    # Can't operate without these parameters.
    if not options.app_key or not options.app_secret:
        parser.error('You must obtain an app key and secret from Dropbox at the following URL.\n\nhttps://www.dropbox.com/developers/apps')

    # Instantiate a client one way or another.
    if not options.token_key and not options.token_secret:
        s = session.DropboxSession(app_key, app_secret, access_type)
        # Get a temporary token, so we can make oAuth calls.
        t = s.obtain_request_token()
        print "Please visit the following URL and authorize this application.\n"
        print s.build_authorize_url(t)
        print "\nWhen you are done, please press <enter>."
        raw_input()
        # Trade up to permanent access token.
        a = s.obtain_access_token(t)
        token_key, token_secret = a.key, a.secret
        print 'Your access token will be printed below, store it for later use.'
        print 'For future accesses, you can pass the --token-key and --token-secret'
        print ' arguments.\n'
        print 'Access token:', a.key
        print 'Access token secret:', a.secret
        print "\nWhen you are done, please press <enter>."
        raw_input()
    elif not options.token_key or not options.token_secret:
        parser.error('You must provide both the access token and the access token secret.')
    else:
        token_key, token_secret = options.token_key, options.token_secret

    fs = DropboxFS(options.app_key, options.app_secret, options.type, token_key, token_secret)
    print fs.listdir('/')

if __name__ == '__main__':
    main()
