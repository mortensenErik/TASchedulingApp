from django.test import TestCase
from app.models import Course
from classes.CourseClass import *

class TestCourse(TestCase):

    def setUp(self):
        self.CS361 = Course.objects.create(CourseId="123", name="Introduction to Software Engineering", number="361",
                                          subject="CS")
        self.CS250 = Course.objects.create(CourseId="124", name="Introductory Computer Programming", number="250", subject="CS")
        self.CS251 = Course.objects.create(CourseId="125", name="Intermediate Computer Programming", number="251", subject="CS")

    def test_course_made(self):
        test = CourseClass.createCourse(CourseId="126", name="Data Structures and Algorithms", number="351", subject="CS")
        lookup = list(Course.objects.all())
        self.assertEqual(len(lookup), 4, msg="Error: course was not created")

    def test_course_delete(self):
        test = CourseClass.createCourse(CourseId="123", name="Introduction to Software Engineering", number="361", subject="CS")
        lookup = list(Course.objects.all())
        self.assertEqual(len(lookup), 2, msg="Error: course was not deleted")
