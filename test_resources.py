import unittest
from resources import Resource, load_default_resources

class TestResources(unittest.TestCase):

    def test_returns_list(self):
        resources = load_default_resources()

        self.assertIsInstance(resources, list)
    
    def test_resource_count(self):
        resources = load_default_resources()

        self.assertEqual(len(resources), 4)

    def test_items_are_resources(self):
        resources = load_default_resources()

        for item in resources:
            self.assertIsInstance(item, Resource)
    
    def test_resource_fields(self):
        resources = load_default_resources()

        firstResource = resources[0]

        self.assertEqual(firstResource.name, "XULA Academic Calendar")
        self.assertEqual(firstResource.url, "https://www.xula.edu/academics/calendar")
        self.assertEqual(firstResource.category, "Academics")
        self.assertEqual(firstResource.icon, "calendar")



