import urllib2
try:
    import json as simplejson  # For Python 2.6+
except ImportError:
    import simplejson  # NOQA

API_BASE_URL = 'https://www.kanbanpad.com/api/v1'


class KanbanpadRequest(object):

    def __init__(self, username=None, api_key=None, api_base_url=None):
        self.username = username
        self.api_key = api_key
        self.api_base_url = api_base_url or API_BASE_URL
        self.response_format = 'json'

        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, self.api_base_url, self.username,
                self.api_key)
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

    def get(self, url):
        try:
            response = urllib2.urlopen(url)
            return simplejson.loads(response.read())
        except urllib2.URLError:
            return False
