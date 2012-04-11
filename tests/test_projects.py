import unittest
from kanbanpad.projects import Project


class ProjectsTestCase(unittest.TestCase):

    def test_model(self):
        data = {"organization_id": None, "wip_limit": 10,
                "slug": "0d51662f803c8a3b3713",
                "email": "onjinx@gmail.com", "name": "Untitled",
                "privacy": 0, "created_at": "2012-04-11T09:04:08Z",
                "id": "4f8549074075cd000f02cc1e",
                "updated_at": "2012-04-11T20:50:31Z"}

        project = Project.from_json(data)

        for key in data:
            self.assertEqual(getattr(project, key), data[key])
