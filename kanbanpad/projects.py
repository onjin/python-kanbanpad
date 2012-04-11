from kanbanpad.core import Manager
import simplejson as json


class Project(object):
    __slots__ = [
            'id',
            'wip_limit',
            'name',
            'privacy',
            'created_at',
            'updated_at',
            'slug',
            'organization_id',
            'email',
        ]

    def __init__(self):
        pass

    @classmethod
    def from_json(self, data):
        project = Project()

        for key in data:
            setattr(project, key, data[key])
        return project

    def to_json(self):
        data = {}
        [data.update({key: getattr(self, key)}) for key in self.__slots__]
        return json.dumps(data)


class Projects(Manager):

    def all(self):
        return [Project.from_json(data) for data in self.call('projects')]
