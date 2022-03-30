from demo.models.person import Person
import unittest

"""
Unit Test Code 
"""


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("tester", "surname")

    def test_person_creation(self):
        self.assertEqual(self.person.first, "tester",
                         "Failed to create person object")

    def test_person_email_function(self):
        email_template = f"{self.person.first}.{self.person.second}@email.com"
        self.assertEqual(self.person.email, email_template,
                         "email function failed")

    def test_person_display_function(self):
        display_template = f"{self.person.first} {self.person.second}"
        self.assertEqual(self.person.display, display_template,
                         "display function failed")

    def tearDown(self):
        del self.person
        return super().tearDown()
