import locale
import time
import urllib
import urllib2
import hmac
import json
import sys
import binascii
from hashlib import sha1


locale.setlocale(locale.LC_ALL, 'C')


def sap_timestamp(timestamp):
    return time.strftime('%Y.%m.%d %H:%M:%S', timestamp)


def runs_in_sap():
    return sys.executable.endswith(u'al_engine.exe')


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


class OAuth1Helper(object):
    def __init__(self, access_token, access_token_secret,
                 consumer_key, consumer_key_secret):
        self.oauth_access_token = access_token
        self.oauth_access_token_secret = access_token_secret
        self.oauth_consumer_key = consumer_key
        self.oauth_consumer_secret = consumer_key_secret

        self.oauth_nonce = ''
        self.oauth_signature = ''
        self.oauth_signature_method = "HMAC-SHA1"
        self.oauth_timestamp = int(time.time())
        self.oauth_version = "1.0"
        self.method = 'GET'
        self.nonauthParams = {}
        self.oauthparams = {}

    def generate_HMAC(self, raw, key):
        """Generates a HMAC-SHA1 encoded String"""
        hashed = hmac.new(key, raw, sha1)
        return binascii.b2a_base64(hashed.digest())[:-1]

    def generate_header(self):
        """
        returns the String that used in the http request header
        for Authorization
        """
        header = 'OAuth '
        keylist1 = self.oauthparams.keys()
        keylist1.sort()
        for key in keylist1:
            value = self.oauthparams[key]
            header += key + '="' + value + '", '
        header = header.rstrip(', ')
        return header

    def generateHeader(self, url, params):
        """
        is called with the url and the parameters that should be send
        in the request and returns the
        for the authentication needed OAuth Authorization String
        """
        self.createOAuthParams(params)
        self.createSignature(url)
        mergedParams = self.mergeOAuthRequestParam()

        keylist = mergedParams.keys()
        keylist.sort()

        return self.generate_header()

    def mergeOAuthRequestParam(self):
        """
        merges the oauth parameter and the parameters needed
        for the request into on dict and returns this dict
        """
        mergedParams = {}
        keylist1 = self.oauthparams.keys()
        for key in keylist1:
            mergedParams[key] = self.oauthparams[key]

        keylist2 = self.nonauthParams.keys()
        for key in keylist2:
            mergedParams[key] = self.nonauthParams[key]

        mergedParams = self.sortParamsByKey(mergedParams)
        return mergedParams

    def createSignature(self, url):
        """
        creates with the passed parameters and the url the signature
        for the oauth_signature parameter
        """
        mergedParam = self.mergeOAuthRequestParam()
        signature = ''
        signature += self.method.upper() + '&'
        signature += self.escape_param(url) + '&'

        parameterstring = ''
        keylist = mergedParam.keys()
        keylist.sort()
        for key in keylist:
            value = self.escape_param(mergedParam[key])
            parameterstring += str(key) + '=' + str(value) + '&'

        parameterstring = parameterstring.rstrip('&')
        parameterstring = self.escape_param(parameterstring)
        signature += parameterstring
        signingkey = (self.escape_param(self.oauth_consumer_secret) +
                      '&' + self.escape_param(self.oauth_access_token_secret))

        hmaccode = self.generate_HMAC(signature, signingkey)
        self.oauth_signature = hmaccode
        self.oauthparams['oauth_signature'] = self.escape_param(hmaccode)
        self.sortParamsByKey(self.oauthparams)
        return signature

    def createOAuthParams(self, params):
        """initializes the oauthparameter dicts"""
        self.oauth_timestamp = int(time.time())
        self.oauth_nonce = self.generateNonce()
        self.generate_header()
        # encode query parameter
        keylist = params.keys()
        encodedparams = {}
        keylist.sort()
        for key in keylist:
            encodedparams[self.escape_param(key)] = params[self.escape_param(key)]

        # encode oauth params
        oauthparams = {}
        oauthparams['oauth_consumer_key'] = self.escape_param(self.oauth_consumer_key)
        oauthparams['oauth_nonce'] = self.escape_param(str(self.oauth_nonce))
        oauthparams['oauth_signature_method'] = self.escape_param(self.oauth_signature_method)
        oauthparams['oauth_timestamp'] = self.escape_param(str(self.oauth_timestamp))
        oauthparams['oauth_token'] = self.escape_param(self.oauth_access_token)
        oauthparams['oauth_version'] = self.escape_param(self.oauth_version)
        self.sortParamsByKey(oauthparams)
        self.sortParamsByKey(encodedparams)
        self.oauthparams = oauthparams
        self.nonauthParams = encodedparams

    def escape_param(self, param):
        """escapes the urls and parameters"""
        return urllib.quote(str(param), safe='~')

    def sortParamsByKey(self, param):
        keylist = param.keys()
        sortedparams = {}
        keylist.sort()
        for key in keylist:
            sortedparams[key] = param[key]
        return sortedparams

    def generateNonce(self):
        random_number = time.time()

        return str(int(random_number))


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
                        print 'Successfully added {0} to collection'.format(tweet_id)
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


if runs_in_sap():
    PROXY = u'iproxy.corproot.net:8080'
else:
    from sap import Collection, DataManager
    # setup fake input data
    DSRecord = DataManager.NewDataRecord(1)
    DSRecord.SetField(u'TWEET_ID_IN', unicode('0'))
    Collection.AddRecord(DSRecord)



if __name__ == '__main__':
    print 'Start collecting tweets...'

    print 'Loading input task data...'
    searchTermRec = DataManager.NewDataRecord()
    Collection.GetRecord(searchTermRec, 1)
    max_id = searchTermRec.GetField(u'TWEET_ID_IN')
    Collection.DeleteRecord(searchTermRec)
    DataManager.DeleteDataRecord(searchTermRec)

    def swisscom_fr():
        helper = OAuth1Helper(
            access_token='115386140-BjCIEooK9mmm9k5oUntAyLw1YxHTCbRIPVwZzQH7',
            access_token_secret='1WrDzn4gIWZKf3nrSpU9MA0yAEPNMdRdKvPjRO884u0oq',
            consumer_key='UEr0TKR4oW1OMt9kNuUxN32nA',
            consumer_key_secret='KU9xjOfV6mL3pPmQ1KZoOB8MZZgKVdrztWOiRR0MFn0rMUOJZl'
        )
        return TwitterCollector(max_id, 'Swisscom_fr', 115386140, helper)

    def swisscom_b2b_de():
        helper = OAuth1Helper(
            access_token = '268323153-TZBMexArlur68E4hIAvtzy17QvMTMGyvXMar1Z0y',
            access_token_secret = 'J7Zvvy0i35meR2yJeway9ctjLJiCC60OTjCQSRugPgE3R',
            consumer_key = 'orY4X8ni9SjpWbbHZzy7WLQFC',
            consumer_key_secret = 'HORdoxOSnG8U4E1gW6GRutRiqJ1RmOsCydAHSlRp7LY3ZyTwUG',
        )
        return TwitterCollector(max_id, 'swisscom_b2b_de', 268323153, helper)

    print 'Preparing fetch tasks'
    searchCollectors = [swisscom_fr(), swisscom_b2b_de()]

    print 'Total %d tasks to search.\n' % len(searchCollectors)

    print 'Begin data search...'
    for sc in searchCollectors:
        results = sc.search()
        print 'Twitter account {0}. Total tweets collected: {1}'.format(
            sc.screen_name, results)
    print 'Finished collecting tweets using the Twitter API v1.1.'
