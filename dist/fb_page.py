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
        handler = urllib2.ProxyHandler({'http': proxy, 'https': proxy})

    params = urllib.urlencode(queryParams)
    http_body = None if method == 0 else params
    http_url = '%s?%s' % (url, params) if method == 0 else url

    try:
        opener = urllib2.build_opener(handler)

        if oauth_helper:
            head = oauth_helper.generateHeader(url, queryParams)

            opener.addheaders = [('Authorization', head)]
            print(opener.addheaders)

        print 'GET:{0}'.format(http_url)
        data = opener.open(http_url, data=http_body).read()

        try:
            result = json.loads(data)
        except ValueError, e:
            print e
            return None
        return result
    except urllib2.HTTPError, e:
        print(e.read())
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print 'Could not reach %s due to %s.' % (http_url, str(e.reason))
        elif hasattr(e, 'code'):
            print 'Could not fulfill the request due to %s.' % str(e.code)
        return None


def unix_timestamp(timestamp):
    """Convert python time object to unix timestamp"""
    return calendar.timegm(timestamp.utctimetuple())


def sap_timestamp(timestamp):
    return time.strftime('%Y.%m.%d %H:%M:%S', timestamp)


def runs_in_sap():
    return sys.executable.endswith('al_engine.exe')


ACCESS_TOKEN = 'CAAIcqYlr5QMBAEpoQTEqQn6y2qp6z5y1n3aoriTShRwvYo3SsusyWuAaGizqCYtZCmpw90yL5AaneoaDCqzLnZAZC3zbi2ZAdjanWNbLOts5LvcjFZCWRtvbeS5mX67Clyyec3uLZCz3VDiQ87Xyw4o9eMFpDijU5IojmZAo2QiZC0iYbb50uwKB'
PAGE_NAME = 'swisscom'
POST_LIMIT = 5
PROXY = ''
locale.setlocale(locale.LC_ALL, 'C')


class Post(object):
    """Facebook post with metrics"""
    def __init__(self, page_name, id, message, lang, typ, timestamp):
        self.page_name = page_name
        self.id = id
        self.message = message
        self.lang = lang
        self.typ = typ
        self.timestamp = timestamp
        self.metrics = {}  # Insights data

    def __repr__(self):
        return 'Post(id={0}, timestamp={1})'.format(self.id, sap_timestamp(self.timestamp))


def create_record(post):
    """Create DSRecord for post and add to collection"""
    metrics = post.metrics

    engaged_users = metrics[u'post_engaged_users']
    impr_organic = metrics[u'post_impressions_organic']
    impr_organic_unique = metrics[u'post_impressions_organic_unique']
    impr_paid = metrics[u'post_impressions_paid']
    impr_paid_unique = metrics[u'post_impressions_paid_unique']
    impr_viral = metrics[u'post_impressions_viral']
    impr_viral_unique = metrics[u'post_impressions_viral_unique']
    impr = metrics[u'post_impressions']
    impr_unique = metrics[u'post_impressions_unique']

    DSRecord = DataManager.NewDataRecord(1)

    DSRecord.SetField(u'PAGE_NAME', unicode(post.page_name))
    DSRecord.SetField(u'POST_ID', unicode(post.id))
    DSRecord.SetField(u'POST_TEXT', unicode(post.message))
    DSRecord.SetField(u'TYP', unicode(post.typ))
    DSRecord.SetField(u'SPRACHE', unicode(post.lang))
    DSRecord.SetField(u'TIMESTAMP', unicode(sap_timestamp(post.timestamp)))
    DSRecord.SetField(u'POST_ENGAGED_USERS', unicode(engaged_users))
    DSRecord.SetField(u'POST_IMPRESSIONS_ORGANIC', unicode(impr_organic))
    DSRecord.SetField(u'POST_IMPRESSIONS_ORGANIC_UNIQUE', unicode(impr_organic_unique))
    DSRecord.SetField(u'POST_IMPRESSIONS_PAID', unicode(impr_paid))
    DSRecord.SetField(u'POST_IMPRESSIONS_PAID_UNIQUE', unicode(impr_paid_unique))
    DSRecord.SetField(u'POST_IMPRESSIONS_VIRAL', unicode(impr_viral))
    DSRecord.SetField(u'POST_IMPRESSIONS_VIRAL_UNIQUE', unicode(impr_viral_unique))
    DSRecord.SetField(u'POST_IMPRESSIONS', unicode(impr))
    DSRecord.SetField(u'POST_IMPRESSIONS_UNIQUE', unicode(impr_unique))

    # store record
    Collection.AddRecord(DSRecord)
    del DSRecord


class FacebookCollector(object):
    """Collects insights about posts from a Facebook page"""
    BASE_URL = 'https://graph.facebook.com'
    MIN_SINCE = datetime.datetime(2015, 1, 1)

    def __init__(self, access_token, page_name, last_post_time=MIN_SINCE):
        self.access_token = access_token
        self.page_name = page_name
        self.since = unix_timestamp(last_post_time)
        self.params = {'access_token': self.access_token,
                       'limit': POST_LIMIT,
                       'since': self.since,
                       'fields': 'type,message,privacy'}
        self.post_detail_params = {'access_token': self.access_token}

    def parse_post(self, post):
        try:
            # import pdb; pdb.set_trace()
            # message = post[u'message']
            import pdb; pdb.set_trace()
            message = None
            id = post[u'id']
            # lang = post[u'privacy'][u'description']
            lang = None
            typ = post[u'type']
            timestamp = time.strptime(post[u'created_time'],
                                      '%Y-%m-%dT%H:%M:%S+0000')
            return Post(self.page_name, id, message, lang, typ, timestamp)
        except Exception, ex:
            print 'Could not parse post: %s' % ex
            pass

    def add_post_metrics(self, post):
        detail_url = '%s/%s/insights' % (self.BASE_URL, post.id)
        resp = get_data(detail_url, PROXY, None,
                        **self.post_detail_params)
        data = resp[u'data']
        post.metrics = self.extract_metrics(data)

        return post

    def extract_metrics(self, insights):
        """Put metrics into dict with metric name as key"""
        def metric_value(insight):
            try:
                return insight[u'values'][0][u'value']
            except KeyError:
                print 'Metric %s does not have value' % insight[u'name']

        metrics = {}
        for insight in insights:
            metric_name = insight[u'name']
            metrics[metric_name] = metric_value(insight)
        return metrics

    def newest_posts(self):
        """Fetch newest posts from page"""

        try:
            # Get all Posts of Swisscom Page (ID, DATE, TYPE)
            request_url = '{0}/{1}/posts'.format(self.BASE_URL, self.page_name)
            results = get_data(request_url, PROXY,
                               None, **self.params)
            data = results[u'data']
            posts = [self.parse_post(post) for post in data]
            posts = [self.add_post_metrics(post) for post in posts]
            return posts
        except Exception, e:
            print 'Could not fetch posts {0}'.format(e)


if runs_in_sap():
    PROXY = 'iproxy.corproot.net:8080'
else:
    from sap import Collection, DataManager


if __name__ == '__main__':
    print 'Beginning to collect Facebook Posts...'

    print 'Loading input task data...'
    # last_post_record = DataManager.NewDataRecord()
    # Collection.GetRecord(last_post_record, 1)
    # max_id = last_post_record.GetField(u'POST_ID_IN')
    # DataManager.DeleteDataRecord(last_post_record)

    print 'Creating input task for {0}'.format(PAGE_NAME)
    collectors = []
    try:
        collector = FacebookCollector(ACCESS_TOKEN, PAGE_NAME)
        collectors.append(collector)
    except Exception, e:
        print "Error occurred while creating input tasks: %s" % e

    print 'Total %d tasks to search.\n' % len(collectors)

    print 'Begin data search...'
    for collector in collectors:
        results = collector.newest_posts()
        for post in results:
            create_record(post)
            print 'Created record {0}'.format(post)
        print 'The term search finished. Total posts collected: %d.\n' % (len(results))
    print 'Finished collecting Facebook posts'
