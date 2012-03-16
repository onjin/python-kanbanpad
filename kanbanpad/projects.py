from kanbanpad.core import Manager

class Projects(Manager):

    def all(self):
        return self.call('projects')
