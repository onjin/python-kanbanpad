

class Manager(object):
    def __init__(self, request):
        self.request = request

    def call(self, resource, method='GET'):
        url = "%s/%s.%s" % (self.request.api_base_url, resource,
                self.request.response_format)
        response = self.request.get(url)
        return response
