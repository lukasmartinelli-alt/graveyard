import locale
import sys
import time
import urllib
import urllib2
import json


RUNS_IN_SAP = sys.executable.endswith(u'al_engine.exe')
ACCESS_TOKEN = 'AIzaSyBCPXBT29p0GnxvZ-s0kggHmQjENxDHdh8'
USER_ID = 116503069960955784178
BASE_URL = 'https://www.googleapis.com/plus/v1/people'
# MAX_RESULTS = 100
MAX_RESULTS = 5
if RUNS_IN_SAP:
    PROXY = u'iproxy.corproot.net:8080'
    locale.setlocale(locale.LC_ALL, 'C')
else:
    PROXY = u''
    from sap import Collection, DataManager


def sap_timestamp(timestamp):
    return time.strftime('%Y.%m.%d %H:%M:%S', timestamp)


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


class Activity(object):
    def __init__(self, id, published_at, title, replies, plusoners, resharers):
            self.id = id
            self.published_at = published_at
            self.title = title
            self.replies = replies
            self.plusoners = plusoners
            self.resharers = resharers


class GooglePlusFeed(object):
    """Fetches information about public activities of a profile"""
    FIELDS = ('items(access,id,object(content,id,objectType,originalContent,'
              'plusoners/totalItems,replies/totalItems,resharers/totalItems,'
              'url),placeId,placeName,published,title)')

    def __init__(self, access_token, user_id):
        self.access_token = access_token
        self.user_id = user_id

        self.params = {'key': self.access_token,
                       'maxResults': MAX_RESULTS,
                       'fields': self.FIELDS}

    def parse_activity(self, activity):
        obj = activity['object']
        timestamp = time.strptime(activity[u'published'],
                                  '%Y-%m-%dT%H:%M:%S.%fZ')
        print(obj)
        return Activity(
            id=activity['id'],
            published_at=timestamp,
            title=activity['title'],
            replies=obj['replies']['totalItems'],
            plusoners=obj['plusoners']['totalItems'],
            resharers=obj['resharers']['totalItems']
        )

    def newest_activities(self):
        """Fetch newest activities from Google+ profile"""
        collection = 'public'
        request_url = '{0}/{1}/activities/{2}'.format(BASE_URL,
                                                      self.user_id,
                                                      collection)
        response = get_data(request_url, PROXY, None, **self.params)
        items = response['items']
        return [self.parse_activity(i) for i in items]


def create_record(activity):
    rec = DataManager.NewDataRecord(1)

    rec.SetField(u'ACTIVITY_ID', unicode(activity.id))
    rec.SetField(u'TIME_STAMP', unicode(sap_timestamp(activity.published_at)))
    rec.SetField(u'TITLE', unicode(activity.title))
    rec.SetField(u'REPLIES', unicode(activity.replies))
    rec.SetField(u'PLUSONERS', unicode(activity.plusoners))
    rec.SetField(u'RESHARERS', unicode(activity.resharers))

    Collection.AddRecord(rec)
    del rec


if __name__ == '__main__':
    print u'Start collecting Google+ activities...'
    Collection.Truncate()  # clear input collection

    swisscom_profile = GooglePlusFeed(ACCESS_TOKEN, USER_ID)
    feeds = [swisscom_profile]

    print 'Processing {0} input tasks'.format(len(feeds))
    for feed in feeds:
        activities = feed.newest_activities()
        for activity in activities:
            create_record(activity)
            print 'Successfully added {0} to collection'.format(activity.id)
        print '{0} activities fetched.'.format(len(activities))

    print 'Finished collecting Google+ activities'
