from django.test import TestCase
from app.models import Course
from classes.CourseClass import *

class TestCourse(TestCase):

    def setUp(self):
        self.CS361 = Course.objects.create(CourseId="121", name="compscI", number="361", subject="test2")
        self.CS250 = Course.objects.create(CourseId="122", name="compsCi", number="250", subject="test1")
        self.CS251 = Course.objects.create(CourseId="123", name="compSci", number="251", subject="test0")

    def test_course_made(self):
        test = CourseClass.createCourse(CourseId="120", name="comPsci", number="351", subject="test3")
        lookup = list(Course.objects.all())
        self.assertEqual(len(lookup), 4, msg="Error: course was not created")

    def test_course_delete(self):
        test = CourseClass.deleteCourse(CourseId="120")
        lookup = list(Course.objects.all())
        self.assertEqual(len(lookup), 3, msg="Error: course was not deleted.")
