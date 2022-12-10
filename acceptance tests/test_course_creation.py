from django.test import TestCase, Client
from app.models import UserProfile, Course, Section


class testCreateCourse(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.cs361 = Course.objects.create(CourseId='CS361', name='Intro to Software Engineering', number='361',
                                           subject='CompSci')

    def testCreateNewCourse(self):
        self.monkey.post("new_course/", {"CourseId": "10101", "name": "Binary Mathematics", "number": "101", "subject": "CompSci"})
        self.assertEqual(len(Course.objects.filter(CourseId='10101')), 1, msg="Course was not created")


    def testCreateOldCourse(self):
        self.monkey.post("new_course/", {"CourseId": "CS361", "name": "Intro to Software Engineering", "number": "361",
                                         "subject": "CompSci"})
        self.assertEqual(len(Course.objects.filter(CourseId='CS361')), 1, msg="Course already exists")