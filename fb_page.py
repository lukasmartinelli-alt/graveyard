import locale
import time
import datetime
import calendar
from http import get_data
from sap import Collection, DataManager


ACCESS_TOKEN = 'CAAIcqYlr5QMBAEpoQTEqQn6y2qp6z5y1n3aoriTShRwvYo3SsusyWuAaGizqCYtZCmpw90yL5AaneoaDCqzLnZAZC3zbi2ZAdjanWNbLOts5LvcjFZCWRtvbeS5mX67Clyyec3uLZCz3VDiQ87Xyw4o9eMFpDijU5IojmZAo2QiZC0iYbb50uwKB'
PAGE_NAME = 'swisscom'
# PROXY = 'iproxy.corproot.net:8080'
PROXY = ''


def unix_timestamp(timestamp):
    """Convert python time object to unix timestamp"""
    return calendar.timegm(timestamp.utctimetuple())


class Post(object):
    """Facebook post with metrics"""
    def __init__(self, id, message, lang, typ, timestamp):
        self.id = id
        self.message = message
        self.lang = lang
        self.typ = typ
        self.timestamp = timestamp
        self.metrics = {}  # Insights data

    def __repr__(self):
        return 'Post(id={0}, timestamp={1})'.format(self.id, self.timestamp)


class FacebookCollector(object):
    """Collects insights about posts from a Facebook page"""
    BASE_URL = 'https://graph.facebook.com'
    MIN_SINCE = datetime.datetime(2015, 1, 1)

    def __init__(self, access_token, page_name, last_post_time=MIN_SINCE):
        self.access_token = access_token
        self.page_name = page_name
        self.since = unix_timestamp(last_post_time)
        self.params = {'access_token': self.access_token,
                       'limit': 250,
                       'since': self.since,
                       'fields': 'type,message,privacy'}
        self.post_detail_params = {'access_token': self.access_token}

    def parse_post(self, post):
        try:
            # import pdb; pdb.set_trace()
            # message = post[u'message']
            message = None
            id = post[u'id']
            # lang = post[u'privacy'][u'description']
            lang = None
            typ = post[u'type']
            timestamp = post['created_time']
            return Post(id, message, lang, typ, timestamp)
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
        # Do we really need those??
        collectionSize = Collection.Size()
        searchTermRec = DataManager.NewDataRecord()

        try:
            # Get all Posts of Swisscom Page (ID, DATE, TYPE)
            request_url = '{0}/{1}/posts'.format(self.BASE_URL, self.page_name)
            results = get_data(request_url, PROXY,
                               None, **self.params)
            data = results[u'data']
            posts = [self.parse_post(post) for post in data]
            for post in posts:
                post = self.add_post_metrics(post)
                metrics = post.metrics

                engaged_users = metrics[u'post_engaged_users']
                impr_organic = metrics[u'post_impressions_organic']
                impr_organic_unique = metrics[u'post_impressions_organic_unique']
                impr_paid = metrics['post_impressions_paid']
                impr_paid_unique = metrics['post_impressions_paid_unique']
                impr_viral = metrics['post_impressions_viral']
                impr_viral_unique = metrics['post_impressions_viral_unique']
                impr = metrics['post_impressions']
                ipr_unique = metrics['post_impressions_unique']

                print(post)
                print(metrics)

            return posts
        except Exception, e:
            print 'Could not fetch posts {0}'.format(e)
            raise

# Begin Search Job
print 'Beginning to collect Facebook Posts...'

locale.setlocale(locale.LC_ALL, 'C')

print 'Loading input task data...'
collectionSize = Collection.Size()
searchTermRec = DataManager.NewDataRecord()
collectors = []

Collection.GetRecord(searchTermRec, 1)
max_id = searchTermRec.GetField(u'POST_ID_IN')
try:
    print 'Preparing search task'
    sc = FacebookCollector(ACCESS_TOKEN, PAGE_NAME)
    collectors.append(sc)
    # delete this dataRecord
    Collection.DeleteRecord(searchTermRec)
except Exception, e:
    print "Error occurred while preparing input tasks: %s" % e

DataManager.DeleteDataRecord(searchTermRec)
print 'Total %d tasks to search.\n' % len(collectors)

print 'Begin data search...'
for sc in collectors:
    results = sc.newest_posts()
    print 'The term search finished. Total posts collected: %d.\n' % (len(results))
print 'Finished collecting Facebook posts'
