from kanbanpad.request import KanbanpadRequest
from kanbanpad.projects import Projects


class KanbanpadClient(object):

    def __init__(self, username=None, api_key=None, api_base_url=None):
        self.request = KanbanpadRequest(username=username, api_key=api_key,
                api_base_url=api_base_url)
        self.projects = Projects(self.request)
