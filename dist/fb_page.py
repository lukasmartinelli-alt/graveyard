import locale
import datetime
import time
import calendar
import json
import urllib
import urllib2
import sys


def get_data(url, proxy, oauth_helper, method=0, **queryParams):
    """
    Send an http or https request and receive a JSON object if
    there is no error.
    """

    handler = urllib2.BaseHandler()
    # Determine if the request must use a proxy
    if proxy is not None and proxy != '':
        handler = urllib2.ProxyHandler({u'http': proxy, u'https': proxy})

    params = urllib.urlencode(queryParams)
    http_body = None if method == 0 else params
    http_url = u'%s?%s' % (url, params) if method == 0 else url

    try:
        opener = urllib2.build_opener(handler)

        if oauth_helper:
            head = oauth_helper.generateHeader(url, queryParams)

            opener.addheaders = [(u'Authorization', head),
                                 (u'Accept-Charset', 'utf-8')]
            print(opener.addheaders)

        print u'GET {0}'.format(http_url)
        data = opener.open(http_url, data=http_body).read()

        try:
            result = json.loads(data, encoding='utf-8')
        except ValueError, e:
            print u'Could not load JSON: {0}'.format(e)
            return None
        return result
    except urllib2.HTTPError, e:
        print e.read()
    except urllib2.URLError, e:
        if hasattr(e, u'reason'):
            print u'Could not reach %s due to %s.' % (http_url, str(e.reason))
        elif hasattr(e, u'code'):
            print u'Could not fulfill the request due to %s.' % str(e.code)
        return None


def unix_timestamp(timestamp):
    """Convert python time object to unix timestamp"""
    return calendar.timegm(timestamp.utctimetuple())


def sap_timestamp(timestamp):
    return time.strftime('%Y.%m.%d %H:%M:%S', timestamp)


def runs_in_sap():
    return sys.executable.endswith(u'al_engine.exe')


locale.setlocale(locale.LC_ALL, 'C')
PAGE_NAME = u'swisscom'
POST_LIMIT = 3
PROXY = u''
ACCESS_TOKEN = (u'CAAIcqYlr5QMBAEpoQTEqQn6y2qp6z5y1n3aoriTShRwvYo3SsusyWuAaGiz'
                u'qCYtZCmpw90yL5AaneoaDCqzLnZAZC3zbi2ZAdjanWNbLOts5LvcjFZCWRtv'
                u'beS5mX67Clyyec3uLZCz3VDiQ87Xyw4o9eMFpDijU5IojmZAo2QiZC0iYbb5'
                u'0uwKB')


class Post(object):
    """Facebook post with metrics"""
    def __init__(self, page_name, id, message, lang, typ, timestamp):
        self.page_name = page_name
        self.id = id
        self.message = message[:100]
        self.lang = lang
        self.typ = typ
        self.timestamp = timestamp
        self.metrics = {}  # Insights data

    def __repr__(self):
        return u'Post(id={0}, timestamp={1}, typ={2}, message={3})'.format(
            self.id, sap_timestamp(self.timestamp),
            self.typ, self.message
        )


def create_record(post):
    """Create DSRecord for post and add to collection"""

    DSRecord = DataManager.NewDataRecord(1)

    DSRecord.SetField(u'PAGE_NAME', post.page_name)
    DSRecord.SetField(u'POST_ID', post.id)
    DSRecord.SetField(u'TYP', post.typ)
    DSRecord.SetField(u'SPRACHE', post.lang)
    DSRecord.SetField(u'TIMESTAMP', sap_timestamp(post.timestamp))

    # can raise error for utf-8 chars
    DSRecord.SetField(u'POST_TEXT', post.message)

    metrics = post.metrics

    print vars(post)

    engaged_users = metrics.get(u'post_engaged_users', 0)
    impr_organic = metrics.get(u'post_impressions_organic', 0)
    impr_organic_unique = metrics.get(u'post_impressions_organic_unique', 0)
    impr_paid = metrics.get(u'post_impressions_paid', 0)
    impr_paid_unique = metrics.get(u'post_impressions_paid_unique', 0)
    impr_viral = metrics.get(u'post_impressions_viral', 0)
    impr_viral_unique = metrics.get(u'post_impressions_viral_unique', 0)
    impr = metrics.get(u'post_impressions', 0)
    impr_unique = metrics.get(u'post_impressions_unique', 0)

    DSRecord.SetField(u'POST_ENGAGED_USERS', engaged_users)
    DSRecord.SetField(u'POST_IMPRESSIONS_ORGANIC', impr_organic)
    DSRecord.SetField(u'POST_IMPRESSIONS_ORGANIC_UNIQUE', impr_organic_unique)
    DSRecord.SetField(u'POST_IMPRESSIONS_PAID', impr_paid)
    DSRecord.SetField(u'POST_IMPRESSIONS_PAID_UNIQUE', impr_paid_unique)
    DSRecord.SetField(u'POST_IMPRESSIONS_VIRAL', impr_viral)
    DSRecord.SetField(u'POST_IMPRESSIONS_VIRAL_UNIQUE', impr_viral_unique)
    DSRecord.SetField(u'POST_IMPRESSIONS', impr)
    DSRecord.SetField(u'POST_IMPRESSIONS_UNIQUE', impr_unique)

    # store record
    print 'About to add {0} to collection'.format(post.id)
    Collection.AddRecord(DSRecord)
    print 'Successfully added {0} to collection'.format(post.id)


class FacebookPage(object):
    """Collects insights about posts from a Facebook page"""
    BASE_URL = u'https://graph.facebook.com'
    MIN_SINCE = datetime.datetime(2015, 1, 1)

    def __init__(self, access_token, page_name, last_post_time=MIN_SINCE):
        self.access_token = access_token
        self.page_name = page_name
        self.since = unix_timestamp(last_post_time)
        self.params = {u'access_token': self.access_token,
                       u'limit': POST_LIMIT,
                       u'since': self.since,
                       u'fields': u'type,message,privacy'}
        self.post_detail_params = {u'access_token': self.access_token}

    def parse_post(self, post):
        try:
            id = post[u'id']
            message = None
            lang = None
            typ = post[u'type']

            timestamp = time.strptime(post[u'created_time'],
                                      '%Y-%m-%dT%H:%M:%S+0000')

            if u'message' in post:
                message = post[u'message']

            # lang = post[u'privacy'][u'description']

            return Post(self.page_name, id, message, lang, typ, timestamp)
        except Exception, ex:
            print u'Could not parse post: %s' % ex
            pass

    def add_post_metrics(self, post):
        detail_url = u'{0}/{1}/insights'.format(self.BASE_URL, post.id)
        try:
            resp = get_data(detail_url, PROXY, None, **self.post_detail_params)
            data = resp[u'data']
            post.metrics = self.extract_metrics(data)
        except Exception, e:
            print 'Could not fetch post metrics: {0}'.format(e)
        return post

    def extract_metrics(self, insights):
        """Put metrics into dict with metric name as key"""
        def metric_value(insight):
            try:
                return insight[u'values'][0][u'value']
            except KeyError:
                print u'Metric %s does not have value' % insight[u'name']

        metrics = {}
        for insight in insights:
            metric_name = insight[u'name']
            metrics[metric_name] = metric_value(insight)
        return metrics

    def newest_posts(self):
        """Fetch newest posts from page"""

        try:
            # Get all Posts of Swisscom Page (ID, DATE, TYPE)
            request_url = u'{0}/{1}/feed'.format(self.BASE_URL, self.page_name)
            results = get_data(request_url, PROXY,
                               None, **self.params)
            data = results[u'data']
            posts = [self.parse_post(post) for post in data]
            posts = [self.add_post_metrics(post) for post in posts]
            return posts
        except Exception, e:
            print u'Could not fetch posts {0}'.format(e)
            return []


if runs_in_sap():
    PROXY = u'iproxy.corproot.net:8080'
else:
    from sap import Collection, DataManager


if __name__ == '__main__':
    print u'Start collecting Facebook Posts...'

    # print u'Loading input task data...'
    # last_post_record = DataManager.NewDataRecord()
    # Collection.GetRecord(last_post_record, 1)
    # max_id = last_post_record.GetField(u'POST_ID_IN')
    # DataManager.DeleteDataRecord(last_post_record)

    pages = []
    print u'Creating input task for {0}'.format(PAGE_NAME)
    page = FacebookPage(ACCESS_TOKEN, PAGE_NAME)
    pages.append(page)

    print u'Total %d tasks to search.\n' % len(pages)

    for page in pages:
        print u'Fetch newest posts for page {0}...'.format(page.page_name)
        newest_posts = page.newest_posts()
        for post in newest_posts:
            print u'Creating record {0}'.format(post)
            create_record(post)
        print u'Page {0} finished. Total posts collected: {1}.'.format(
            page.page_name, len(newest_posts))
    print u'Finished collecting Facebook posts'
