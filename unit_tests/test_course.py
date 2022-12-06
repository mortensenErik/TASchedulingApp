from django.test import TestCase
from app.models import Course, UserProfile
from classes import Course
from classes.CourseClass import make_course, delete_course, assign_instructor_to_course

class TestCourse(TestCase):

    def setUp(self):
        self.rock = UserProfile.objects.create(name = "Jay Rock", id = "12", email = "fs", phone = 'test', officeHours = 'test', role = 'test')
        self.sorenson = UserProfile.objects.create(name="Bob Sorenson", id = "11", email = "fs", phone = "test", officeHours = "test", role = "test")
        self.CS361 = Course.objects.create(name = "compsci", number = "361", id = "12343", instructor = self.rock["name"])
        self.CS250 = Course.objects.create(name="compsci", number="250", id="12344", instructor = self.sorenson["name"])
        self.CS251 = Course.objects.create(name = "compsci", number = "251", id = "12346", instructor = self.sorenson["name"])

    def test_course_made(self):
        test = make_course({{"id": "12345"}, {"name": "compsci"}, {"number": "351"}, {"instructor": self.sorenson["name"]}})
        self.assertTrue(test, msg = "Error: trying to create a course that already exists")
        lookup = list(Course.objects.filter(name = "compsci", number = "351"))
        self.assertEqual(len(lookup), 1, msg = "Error: course was not added")
        update = list(Course.objects.filter(name = "compsci"))
        self.assertEqual(len(update), 4)

    def test_course_delete(self):
        test = delete_course({{"id": "12343"}, {"name": "compsci"}, {"number": "361"}, {"instructor": self.rock["name"]}})
        self.assertTrue(test, msg="Error: unable to delete course")
        lookup = list(Course.objects.filter(name = "compsci", number = "361", instructor = self.rock["name"]))
        self.assertEqual(len(lookup), 0, msg = "Error: course was not removed from database")
        update = list(Course.objects.filter(name = "compsci"))
        self.assertEqual(len(update), 2)

    def test_course_assign(self):
        test = assign_instructor_to_course({{"id: 12343"}, {"name": "compsci"}, {"number": "361"}, {"instructor": self.sorenson["name"]}})
        self.assertTrue(test, msg = "Error, unable to assign instructor to course")
        lookup = list(Course.objects.filter(id = "12343", name = "compsci", number = "361", instructor = self.rock["name"]))
        self.assertEqual(len(lookup), 0, msg = "Error: unable to update old instructor with new instructor")

