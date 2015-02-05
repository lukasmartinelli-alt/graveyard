
import json
import urllib
import urllib2


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
        print 'build_opener'

        head = oauth_helper.generateHeader(url, queryParams)
        print 'generate Header'

        opener.addheaders = [('Authorization', head)]
        print(opener.addheaders)
        print 'addheaders'

        data = opener.open(http_url, data=http_body).read()
        print 'open...'
        print http_url

        try:
            result = json.loads(data)
        except ValueError:
            print 'Value Error'
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