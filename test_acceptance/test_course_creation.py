from django.test import TestCase, Client
from app.models import Course


class testCreateCourse(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.cs361 = Course.objects.create(name='Intro to Software Engineering', number='361',
                                           subject='COMPSCI')

    def testCreateNewCourse(self):
        self.monkey.post("/new_course/", {"name": "Binary Mathematics", "number": "101",
                                          "subject": "COMPSCI"})
        self.assertEqual(len(Course.objects.filter(name="Binary Mathematics")), 1, msg="Course was not created")

    def testCreateOldCourse(self):
        with self.assertRaises(ValueError, msg="Multiple identical courses were created") as context:
            self.monkey.post("/new_course/", {"name": "Intro to Software Engineering", "number": "361",
                                              "subject": "COMPSCI"})
