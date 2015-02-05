import locale
import time
from oauth import OAuth1Helper
from http import get_data
from sap import Collection, DataManager


class TwitterCollector(object):
    """Collects tweets from Twitter"""
    def __init__(self, max_tweet, screen_name, user_id, oauth_helper):
        self.since_id = int(max_tweet)
        self.screen_name = screen_name
        self.user_id = user_id
        self.proxy = ''
        # self.proxy = 'iproxy.corproot.net:8080'
        self.oauth_helper = oauth_helper

        baseurl = 'https://api.twitter.com/1.1/'
        self.requestUrl = baseurl + 'statuses/user_timeline.json'

        self.params = {'screen_name': self.screen_name,
                       'user_id': self.user_id}

        if self.since_id > 0:
            self.params['since_id'] = self.since_id

    def search(self):
        twitters = 0
        current_page = 1

        try:
            while True:
                search_results = get_data(self.requestUrl, self.proxy,
                                          self.oauth_helper, **self.params)
                # Stop searching if there are no more results
                if search_results is None or len(search_results) == 0:
                    print 'No additional tweets are available.'
                    break
                else:
                    print 'Processing %d tweets.' % len(search_results)

                # tweet information
                for innerIndex in (range(len(search_results))):
                    sResult = search_results[innerIndex]

                    # read ID
                    tweet_id = sResult[u'id_str']

                    # read content
                    text = sResult[u'text']
                    text = text.replace('\n', '')

                    # read screen name of poster
                    user = sResult[u'user']
                    screen_name = user[u'screen_name']

                    # read and format creation date
                    created_at = sResult[u'created_at']
                    if created_at is None:
                        continue

                    timestamp = time.strptime(sResult[u'created_at'],
                                              '%a %b %d %H:%M:%S +0000 %Y')
                    created_at = time.strftime('%Y.%m.%d %H:%M:%S', timestamp)

                    # read retweets and favorites
                    retweets = int(sResult[u'retweet_count'])
                    favourites = int(sResult[u'favorite_count'])

                    # read Follower and Friends count of poster
                    followers_count = int(user[u'followers_count'])
                    friends_count = int(user[u'friends_count'])

                    try:
                        # Move read Data to record
                        DSRecord = DataManager.NewDataRecord(1)
                        DSRecord.SetField(u'SCREEN_NAME', unicode(screen_name))
                        DSRecord.SetField(u'TIME_STAMP', unicode(created_at))

                        DSRecord.SetField(u'TWEET_ID', unicode(tweet_id))

                        DSRecord.SetField(u'TWEET_TEXT', unicode(text) if len(text) <= 140 else unicode(text[:140]))

                        DSRecord.SetField(u'FAV_COUNT', unicode(favourites))
                        DSRecord.SetField(u'RETWEETS', unicode(retweets))

                        DSRecord.SetField(u'FOLLOWERS_COUNT', unicode(followers_count))
                        DSRecord.SetField(u'FRIENDS_COUNT', unicode(friends_count))

                        # store record
                        Collection.AddRecord(DSRecord)
                        del DSRecord

                        # set record size
                        twitters += 1
                    except Exception, e:
                        print 'Error occurred while saving tweet data: %s' % e

                current_page += 1
                print 'There are no more result pages. Ending the search for this term.'
                break
                print '-----------------------------------'
        except Exception, e:
            print e

        return twitters

ACCESS_TOKEN = '115386140-BjCIEooK9mmm9k5oUntAyLw1YxHTCbRIPVwZzQH7'
TOKEN_SECRET = '1WrDzn4gIWZKf3nrSpU9MA0yAEPNMdRdKvPjRO884u0oq'
CONSUMER_KEY = 'UEr0TKR4oW1OMt9kNuUxN32nA'
CONSUMER_SECRET = 'KU9xjOfV6mL3pPmQ1KZoOB8MZZgKVdrztWOiRR0MFn0rMUOJZl'

# Begin Search Job
print 'Beginning to collect Twitter tweets...'

locale.setlocale(locale.LC_ALL, 'C')

print 'Loading input task data...'
collectionSize = Collection.Size()
searchTermRec = DataManager.NewDataRecord()
searchCollectors = []

Collection.GetRecord(searchTermRec, 1)
max_id = searchTermRec.GetField(u'TWEET_ID_IN')
try:
    print 'Preparing search task'
    helper = OAuth1Helper(ACCESS_TOKEN, TOKEN_SECRET,
                          CONSUMER_KEY, CONSUMER_SECRET)
    sc = TwitterCollector(max_id, 'Swisscom_fr', 115386140, helper)
    searchCollectors.append(sc)
    Collection.DeleteRecord(searchTermRec)
except Exception, e:
    print "Error occurred while preparing input tasks: %s" % e

DataManager.DeleteDataRecord(searchTermRec)
print 'Total %d tasks to search.\n' % len(searchCollectors)

print 'Begin data search...'
for sc in searchCollectors:
    results = sc.search()
    print 'The term search finished. Total tweets collected: %d.\n' % (results)
print 'Finished collecting Twitter tweets using the Twitter API v1.1.'
