import json
import urllib
import urllib2
import locale
import time
import hmac
import binascii
from hashlib import sha1

class OAuth1Helper(object):
    def __init__(self):
       
        #self.oauth_consumer_key = 'oyveJx1aWvVn1Rjb1SGL0NuJd'
        #self.oauth_consumer_secret = '1N6HRGIH99q4K1tt3RILIGxOA7cBAKUSpBxpBc2m7Ju101Q8zE'
        self.oauth_access_token = 'CAACEdEose0cBAOvXfYrGselfh7ZC4Tp4KvcsGk2XcgEMI6ykvfMCWvyoo5jHnZC0hkNRJofcxsM2Yb3sfYlZBtE5cyauf5n0XXZBli87Xlt7nldaWP3QiS9Tmko4BvX3JYZBr79ZB5cWZBCwp782x1uVJBXqWgsl69hkynv3hy0BdVekfjvLIZAUiSJMezVHBpOmkNNj4apefVVYCyO6ZB89DAfOLpkieW44ZD'
        #self.oauth_access_token_secret = 'GlPDk4Ekul1fPDGq8tTHjqkBMmPKkAIZrWB0oVvbkyibN'
        self.page = 'swisscom'
        self.oauth_nonce = ''
        self.oauth_signature = ''
        self.oauth_signature_method = "HMAC-SHA1"
        self.oauth_timestamp = int(time.time())
        self.oauth_version = "1.0"
        self.method = 'GET'
        self.nonauthParams = {}
        self.oauthparams = {}

    def generateHMAC(self, raw, key):
        """
        Generates a HMAC-SHA1 encoded String
        """
        hashed = hmac.new(key, raw, sha1)
        return binascii.b2a_base64(hashed.digest())[:-1]

    def generate_header(self):
        """
        returns the String that used in the http request header for Authorization
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
        is called with the url and the parameters that should be send in the request and returns the
            for the authentication needed OAuht Authorization String
        """
        self.createOAuthParams(params)
        self.createSignature(url)
        mergedParams = self.mergeOAuthRequestParam()

        keylist = mergedParams.keys()
        keylist.sort()

        return self.generate_header()

    def mergeOAuthRequestParam(self):
        """
        merges the oauth parameter and the parameters needed for the request into on dict and returns this dict
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
        creates with the passed parameters and the url the signature for the oauth_signature parameter
        """
        mergedParam = self.mergeOAuthRequestParam()
        signature = ''
        signature += self.method.upper() + '&'
        signature += self.escapeParamter(url) + '&'

        parameterstring = ''
        keylist = mergedParam.keys()
        keylist.sort()
        for key in keylist:
            value = self.escapeParamter(mergedParam[key])
            parameterstring += str(key) + '=' + str(value) + '&'

        parameterstring = parameterstring.rstrip('&')
        parameterstring = self.escapeParamter(parameterstring)
        signature += parameterstring
        #signingkey = self.escapeParamter(self.oauth_consumer_secret) + '&' + self.escapeParamter(self.oauth_access_token_secret)

        #hmaccode = self.generateHMAC(signature, signingkey)
        hmaccode = self.generateHMAC(signature, '')
        self.oauth_signature = hmaccode
        self.oauthparams['oauth_signature'] = self.escapeParamter(hmaccode)
        self.sortParamsByKey(self.oauthparams)

    def createOAuthParams(self, params):
        """
        initializes the oauthparameter dicts
        """
        self.oauth_timestamp = int(time.time())
        self.oauth_nonce = self.generateNonce()
        self.generate_header()
        #encode query parameter
        keylist = params.keys()
        encodedparams = {}
        keylist.sort()
        for key in keylist:
            encodedparams[self.escapeParamter(key)] = params[self.escapeParamter(key)]

        #encode oauth params
        oauthparams = {}
        #oauthparams['oauth_consumer_key'] = self.escapeParamter(self.oauth_consumer_key)
        oauthparams['oauth_nonce'] = self.escapeParamter(str(self.oauth_nonce))
        oauthparams['oauth_signature_method'] = self.escapeParamter(self.oauth_signature_method)
        oauthparams['oauth_timestamp'] = self.escapeParamter(str(self.oauth_timestamp))
        oauthparams['oauth_token'] = self.escapeParamter(self.oauth_access_token)
        oauthparams['oauth_version'] = self.escapeParamter(self.oauth_version)
        self.sortParamsByKey(oauthparams)
        self.sortParamsByKey(encodedparams)
        self.oauthparams = oauthparams
        self.nonauthParams = encodedparams

    def escapeParamter(self, para):
        """
        escapes the urls and parameters
        """
        return urllib.quote(str(para), safe='~')

    def convertToUtf8_str(self, string):
        return string.encode("utf-8")

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

class SearchError(StandardError):
    def __init__(self, error):
        self.error = error
        StandardError.__init__(self, error)

def getData(url, proxy, oauth, method=0, **queryParams):
    # Send an http or https request and receive a JSON object if there is no error.

    handler = urllib2.BaseHandler()
    # Determine if the request must use a proxy
    if proxy is not None and proxy != '':
        handler = urllib2.ProxyHandler({'http': proxy, 'https': proxy})

    params = urllib.urlencode(queryParams)
    http_body = None if method == 0 else params
    http_url = '%s?%s' % (url, params) if method == 0 else url   

    try:     
        opener = urllib2.build_opener(handler)
        print 'build_opener'
        
        # pass to the oauth helper the baseurl without parameter + NOT encoded parameter dict
        head = oauth.generateHeader(url, queryParams)
        print 'generate Header'
        
        opener.addheaders = [('Authorization', head)]                     
        print 'addheaders'
        
        data = opener.open(http_url, data=http_body).read()
        print 'open...'
        print http_url
        
        try:
            # Parse data          
            result = json.loads(data)
        except ValueError:
            print 'Value Error'
            return None
        return result
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print 'Failed to reach the %s server due to %s.' % (http_url, str(e.reason))
        elif hasattr(e, 'code'):
            print 'The server could not fulfill the request due to %s.' % str(e.code)
        return None

# Collects tweets from Twitter
class TwitterCollector(object):
    def __init__(self):
        self.since_id    = '2015-01-11'
        self.screen_name = 'swisscom'
        self.user_id     = '20900787629'
        self.proxy        = 'iproxy.corproot.net:8080'
        self.requestUrl  = 'https://graph.facebook.com/swisscom/posts'
        self.access_token = 'CAACEdEose0cBAOvXfYrGselfh7ZC4Tp4KvcsGk2XcgEMI6ykvfMCWvyoo5jHnZC0hkNRJofcxsM2Yb3sfYlZBtE5cyauf5n0XXZBli87Xlt7nldaWP3QiS9Tmko4BvX3JYZBr79ZB5cWZBCwp782x1uVJBXqWgsl69hkynv3hy0BdVekfjvLIZAUiSJMezVHBpOmkNNj4apefVVYCyO6ZB89DAfOLpkieW44ZD'
        self.oauthHelper  = OAuth1Helper()
        self.params       = {'access_token': self.access_token, 'limit': 100000, 'since': self.since_id, 'fields': 'type,message,privacy'} 
        self.post_detail_params  = {'access_token': self.access_token }

    def search(self):
        twitters = 0
        next_page = None
        
        collectionSize = Collection.Size()
        searchTermRec = DataManager.NewDataRecord()
        next_max_id = 0
        min_id = None
        current_page = 1
        posts = []
        
        try:
            x = 1
            #Get all Posts of Swisscom Page (ID, DATE, TYPE)
            search_results = getData(self.requestUrl, self.proxy, self.oauthHelper, **self.params)
            data = search_results[u'data']
            for post in data:    
                #READ GENERAL DATA
                try:
                    print '------------------------------------------------------------START POST------------------------------------------------------------------'
                    print post
                    print '------------------------------------------------------------END POST--------------------------------------------------------------------'
                    
                    #print '------------------------------------------------------------START MESSAGE------------------------------------------------------------------'
                    #print
                    #print '------------------------------------------------------------END MESSAGE------------------------------------------------------------------'
                    
                    post_message =  post[u'message']
                    print 'MESSAGE'
                    print post_message[0:35]
                    print post_message
                    
                    post_id = post[u'id']
                    print 'ID:'
                    print post_id
                   
                    post_language = post[u'privacy'][u'description']
                    print 'LANGUAGE'
                    print post_language
                   
                    post_typ = post[u'type']
                    print 'TYPE'
                    print post_typ
                   
                    post_timestamp = post['created_time']
                    print 'TIME'
                    print post_timestamp
                    
                    
                except Exception, ex:
                    print 'NO MESSAGE'
                    pass
               
                #posts.append({'id:':post_id, 'typ':post_typ, 'timestamp':post_timestamp, 'typ':post_message, 'typ':post_language})
                """for post in data:          
                   
                   # GET POST DETAILS
                   if not post[u'id'] is None:
                       print 'ID:'
                       print post[u'id']
                       #Check if Page commented on a photo / post (No exception thrown)
                       try:
                         story = post[u'story']
                       # Normal post
                       except KeyError:
                         print 'GET POST DETAILS'
                         detail_url = 'https://graph.facebook.com/%s/insights' %(post[u'id'])
                         params = {}
                         post_detailsResponse = getData(detail_url, self.proxy, self.oauthHelper, **self.post_detail_params)
                         post_detailsData = post_detailsResponse[u'data']
                         print post_detailsData
                         for element in post_detailsData:
                            print element
                            if element['name'] == 'page_fans':
                               print 'page_fans'
                               print element[u'values'][0][u'value']
                             
                            elif element['name'] == 'post_engaged_users':
                               print 'post_engaged_users'
                               print element[u'values'][0][u'value']
                             
                            elif element['name'] == 'post_impressions_organic':
                               print 'post_impressions_organic'
                               print element[u'values'][0][u'value']
                             
                            elif element['name'] == 'post_impressions_organic_unique':
                               print 'post_impressions_organic_unique'
                               print element[u'values'][0][u'value']
                               
                            elif element['name'] == 'post_impressions_paid':
                               print 'post_impressions_paid'
                               print element[u'values'][0][u'value']
                             
                            elif element['name'] == 'post_impressions_paid_unique':
                               print 'post_impressions_paid_unique'
                               print element[u'values'][0][u'value']
                             
                            elif element['name'] == 'post_impressions_viral':
                               print 'post_impressions_viral'
                               print element[u'values'][0][u'value']
                             
                            elif element['name'] == 'post_impressions_viral_unique':
                               print 'post_impressions_viral_unique'
                               print element[u'values'][0][u'value']
                             
                            elif element['name'] == 'post_impressions':
                               print 'post_impressions'
                               print element[u'values'][0][u'value']
                             
                            elif element['name'] == 'post_impressions_unique':
                               print 'post_impressions_unique'
                               print element[u'values'][0][u'value']
                     
                   
                       #GET Language
                       print 'GET LANGUAGE'
                       lang_url = 'https://graph.facebook.com/%s/' %(post[u'id'])
                       print lang_url
                       print self.proxy
                       print self.post_detail_params
                       post_detailsLang = getData(detail_url, self.proxy, self.oauthHelper, **self.post_detail_params)
                       language = post_detailsLang['data']['privacy']['description']
                       print 'POST:'
                       print post[u'id']
                       print 'SPRACHE:'
                       print language
                   
                # Stop searching if there are no more results
                if len(search_results) == 0:
                    print 'Ending search since no additional tweets are available.'
                    break
                else:
                    print 'Processing %d tweets.' % len(data)
                
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

                    created_at = time.strftime('%Y.%m.%d %H:%M:%S', time.strptime(sResult[u'created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
                    
                    # read retweets and favorites
                    retweets = int(sResult[u'retweet_count'])
                    favourites = int(sResult[u'favorite_count'])
                    
                    # read Follower and Friends count of poster
                    followers_count = int(user[u'followers_count'])
                    friends_count = int(user[u'friends_count'])
                    
                    
                    try:
                        #Move read Data to record
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
                """
        except SearchError, e:
            print e

        return twitters

# Begin Search Job
print 'Beginning to collect Facebook Posts...'

locale.setlocale(locale.LC_ALL, 'C')

print 'Loading input task data...'
collectionSize = Collection.Size()
searchTermRec = DataManager.NewDataRecord()
searchCollectors = []

Collection.GetRecord(searchTermRec, 1)
max_id = searchTermRec.GetField(u'POST_ID_IN')
try:
  print 'Preparing search task'
  sc = TwitterCollector()        
  searchCollectors.append(sc)

  # delete this dataRecord
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