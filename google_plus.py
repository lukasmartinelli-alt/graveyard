import locale
from http import get_data
from sap import Collection, DataManager


ACCESS_TOKEN = 'AIzaSyBCPXBT29p0GnxvZ-s0kggHmQjENxDHdh8'
USER_ID = 116503069960955784178
# PROXY = 'iproxy.corproot.net:8080'
PROXY = ''


class GooglePlusFeed(object):
    """Fetches information about public activities of a profile"""
    BASE_URL = 'https://www.googleapis.com/plus/v1/people'
    FIELDS = ('items(access,id,object(content,id,objectType,originalContent,'
              'plusoners/totalItems,replies/totalItems,resharers/totalItems,'
              'url),placeId,placeName,published,title)')

    def __init__(self, access_token, user_id):
        self.access_token = access_token
        self.user_id = user_id

        self.params = {'key': self.access_token,
                       'maxResults': 100,
                       'fields': self.FIELDS}

    def newest_activities(self):
        """Fetch newest activities from Google+ profile"""
        collection = 'public'
        request_url = '{0}/{1}/activities/{2}'.format(self.BASE_URL,
                                                      self.user_id,
                                                      collection)
        response = get_data(request_url, PROXY, None, **self.params)
        items = response['items']
        for activity in items:
            id = activity['id'],
            title = activity['title'],
            obj = activity['object']
            replies = obj['replies']['totalItems']
            plusoners = obj['plusoners']['totalItems']
            resharers = obj['resharers']['totalItems']

            print '{0}: +{1}, reshared {2}, replies {3}'.format(
                id, plusoners, resharers, replies)
        return items


print 'Google+ Import started...'
locale.setlocale(locale.LC_ALL, 'C')
swisscom_profile = GooglePlusFeed(ACCESS_TOKEN, USER_ID)
feeds = [swisscom_profile]

print 'Processing {0} input tasks'.format(len(feeds))

for feed in feeds:
    results = feed.newest_activities()
    print '{0} activities fetched.'.format(len(results))

print 'Finished Google+ Import'
