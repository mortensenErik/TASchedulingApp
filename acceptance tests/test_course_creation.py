from django.test import TestCase, Client
from app.models import UserProfile, Course, Section


class testCreateCourse(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.cs361 = Course.objects.create(id='361', name='Intro to Software Engineering', number='CS361',
                                           instructor='nigel')

    def testCreateNewCourse(self):
        self.monkey.post("new_course/", {"id": "10101", "name": "Binary Math", "number": "CS101", "instructor": "Paul"})
        self.assertEqual(len(Course.objects.filter(id='10101')), 1, msg="Course was not created")


    def testCreateOldCourse(self):
        self.monkey.post("new_course/", {"id": "361", "name": "Intro to Software Engineering", "number": "CS361",
                                         "instructor": "Paul"})
        self.assertEqual(len(Course.objects.filter(id='361')), 1, msg="Course already exists")
