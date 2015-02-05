import urllib
import time
import hmac
import binascii
from hashlib import sha1


class OAuth1Helper(object):
    def __init__(self, access_token, access_token_secret, consumer_key, consumer_key_secret):
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
        signingkey = self.escape_param(self.oauth_consumer_secret) + '&' + self.escape_param(self.oauth_access_token_secret)

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
