import locale
import time
import urllib
import urllib2
import hmac
import json
import sys
import binascii
from hashlib import sha1

RUNS_IN_SAP = sys.executable.endswith(u'al_engine.exe')
BASE_URL = 'https://api.twitter.com/1.1/'
TWEET_LIMIT = 200
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


class Tweet(object):
    def __init__(self, screen_name, created_at, id, text, favourites,
                 retweets, followers, friends):
        self.screen_name = screen_name
        self.created_at = created_at
        self.id = id
        self.text = text
        self.favourites = favourites
        self.retweets = retweets
        self.followers = followers
        self.friends = friends


class TwitterUserTimeline(object):
    """Collects tweets from Twitter"""
    def __init__(self, screen_name, user_id, oauth_helper):
        self.screen_name = screen_name
        self.user_id = user_id
        self.oauth_helper = oauth_helper

        self.requestUrl = '{0}/statuses/user_timeline.json'.format(BASE_URL)
        self.params = {'screen_name': self.screen_name,
                       'user_id': self.user_id,
                       'count': TWEET_LIMIT}

    def parse_tweet(self, tweet):
        timestamp = time.strptime(tweet[u'created_at'],
                                  '%a %b %d %H:%M:%S +0000 %Y')
        user = tweet[u'user']

        return Tweet(
            id=tweet[u'id_str'],
            created_at=timestamp,
            text=tweet[u'text'].replace('\n', '')[:140],
            screen_name=user[u'screen_name'],
            retweets=int(tweet[u'retweet_count']),
            favourites=int(tweet[u'favorite_count']),
            followers=int(user[u'followers_count']),
            friends=int(user[u'friends_count'])
        )

    def newest_tweets(self):
        results = get_data(self.requestUrl, PROXY,
                                  self.oauth_helper, **self.params)

        if not results:
            print 'No tweets found for {0}'.format(self.screen_name)
            return []

        return [self.parse_tweet(t) for t in results]


def create_record(tweet):
    rec = DataManager.NewDataRecord(1)

    rec.SetField(u'SCREEN_NAME', unicode(tweet.screen_name))
    rec.SetField(u'TIME_STAMP', unicode(sap_timestamp(tweet.created_at)))
    rec.SetField(u'TWEET_ID', unicode(tweet.id))
    rec.SetField(u'TWEET_TEXT', unicode(tweet.text))
    rec.SetField(u'FAV_COUNT', unicode(tweet.favourites))
    rec.SetField(u'RETWEETS', unicode(tweet.retweets))
    rec.SetField(u'FOLLOWERS_COUNT', unicode(tweet.followers))
    rec.SetField(u'FRIENDS_COUNT', unicode(tweet.friends))

    Collection.AddRecord(rec)
    del rec


def swisscom_de():
    helper = OAuth1Helper(
        consumer_key='oyveJx1aWvVn1Rjb1SGL0NuJd',
        consumer_key_secret='1N6HRGIH99q4K1tt3RILIGxOA7cBAKUSpBxpBc2m7Ju101Q8zE',
        access_token='2813614259-pMRHgmDMxokYqQ0DLsTX82J2IsXhhzdb9hVhp4A',
        access_token_secret='GlPDk4Ekul1fPDGq8tTHjqkBMmPKkAIZrWB0oVvbkyibN'
    )
    return TwitterUserTimeline('Swisscom_de', 98382537, helper)


def swisscom_fr():
    helper = OAuth1Helper(
        consumer_key='UEr0TKR4oW1OMt9kNuUxN32nA',
        consumer_key_secret='KU9xjOfV6mL3pPmQ1KZoOB8MZZgKVdrztWOiRR0MFn0rMUOJZl',
        access_token='115386140-BjCIEooK9mmm9k5oUntAyLw1YxHTCbRIPVwZzQH7',
        access_token_secret='1WrDzn4gIWZKf3nrSpU9MA0yAEPNMdRdKvPjRO884u0oq'
    )
    return TwitterUserTimeline('Swisscom_fr', 115386140, helper)


def swisscom_it():
    helper = OAuth1Helper(
        access_token='115389988-MYkBXTqzBrZL67oXnmQ6XAEFrQYEFKOUE90V3ehf',
        access_token_secret='9m4C8pncSGPgvvIzuFFDcS8EfNdiayhYbqWCgRiqP2tjp',
        consumer_key='41v8vifMt1mGWZAK9H316iAp1',
        consumer_key_secret='Qtw4p8BjIoISzg71WNwWxj81sjIVIarpBY5zVcNZNDmUSuh4Se'
    )
    return TwitterUserTimeline('Swisscom_it', 115389988, helper)


def swisscom_b2b_de():
    helper = OAuth1Helper(
        consumer_key='orY4X8ni9SjpWbbHZzy7WLQFC',
        consumer_key_secret='HORdoxOSnG8U4E1gW6GRutRiqJ1RmOsCydAHSlRp7LY3ZyTwUG',
        access_token='268323153-TZBMexArlur68E4hIAvtzy17QvMTMGyvXMar1Z0y',
        access_token_secret='J7Zvvy0i35meR2yJeway9ctjLJiCC60OTjCQSRugPgE3R'
    )
    return TwitterUserTimeline('swisscom_b2b_de', 268323153, helper)


def swisscom_b2b_fr():
    helper = OAuth1Helper(
        consumer_key='wRpAGlNj60u1fC4ispSxLyn7L',
        consumer_key_secret='BJFqafzl4YF7Daqx4y0rsV86taIsQoIXmAcgy7Ivc5R70bjNsW',
        access_token='270905981-jbOdFr5GYiqv8hUWQky3J918EGGjMT8uTFYiujQB',
        access_token_secret='SQrqiONtaNRJL3YuSSm3ksiMiaCKIN4rzexjQ60dgvxLY'
    )
    return TwitterUserTimeline('swisscom_b2b_fr', 270905981, helper)


def swisscom_b2b_it():
    helper = OAuth1Helper(
        consumer_key='HUgLPizY6eyytVBaXgwcSTKkM',
        consumer_key_secret='gIVkqmfE481aPBlc6doPdeaNJMSKaNaS1v94ZGxudm4hcSjaHI',
        access_token='270906967-cvXwpZ0FHxDk6mopRGBwDQepQ6RQeAAmNb4VfVlA',
        access_token_secret='NeL8q84SrV4mjqXJT0cRJgc2pcVSQDrGNN4MMQb8v43LI'
    )
    return TwitterUserTimeline('swisscom_b2b_it', 270906967, helper)


def swisscom_b2b_en():
    helper = OAuth1Helper(
        consumer_key='N3K26GkPXNaQan5tN9DOQvtTK',
        consumer_key_secret='wLTAbMDdsltFdzrvGZsGZBOvnKdpOyWW144lzSMxJqbxmURc8O',
        access_token='270907679-pDf5svBy6w3e0m3OAbJQaG9xiRuuL7Fq2dC6TKfX',
        access_token_secret='J9G2bL0bp6S2wYtrpQOWQGDzJmGRbHVFJ99dPsaKlGSZS'
    )
    return TwitterUserTimeline('swisscom_b2b_en', 270907679, helper)


if __name__ == '__main__':
    print 'Start collecting tweets...'
    Collection.Truncate()

    print 'Loading input task data...'

    print 'Preparing fetch tasks'
    user_timelines = [swisscom_de(), swisscom_fr(), swisscom_it(),
                      swisscom_b2b_de(), swisscom_b2b_fr(),
                      swisscom_b2b_it(), swisscom_b2b_en()]

    print 'Total %d tasks to search.\n' % len(user_timelines)

    print 'Fetching newest tweets form user timelines...'
    for timeline in user_timelines:
        tweets = timeline.newest_tweets()
        for tweet in tweets:
            create_record(tweet)
            print 'Successfully added {0} to collection'.format(tweet.id)
        print 'Twitter account {0}. Total tweets collected: {1}'.format(
            timeline.screen_name, len(tweets))
    print 'Finished collecting tweets using the Twitter API v1.1.'
