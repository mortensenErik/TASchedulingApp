from django.test import TestCase, Client
from app.models import UserProfile, Course, Section


class TestAdminViewData(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', role="INSTRUCTOR")
        self.frank = UserProfile.objects.create(name='Frank', password='bratwurst', email='frankf@uwm.edu',
                                                phone='202-555-0144', address='abc123', role="TA")
        self.cs361 = Course.objects.create(name='Intro to Software Engineering', number='361',
                                           subject="COMPSCI")
        self.ee457 = Course.objects.create(name='Digital Logic Lab', number='457',
                                           subject="ELECENG")
        self.ee457Lec = Section.objects.create(course=self.ee457, faculty=self.nigel, type='LEC')
        self.cs361Lab = Section.objects.create(course=self.cs361, faculty=self.frank, type='LAB')

    def testViewUsers(self):
        resp = self.monkey.get("/users/")
        self.assertEqual(self.nigel.name, resp.context["users"][0]["name"], msg="Not all users displayed")
        self.assertIn(self.frank.name, resp.context["users"][1]["name"], msg="Not all users displayed")

    def testViewCourses(self):
        resp = self.monkey.get("/courses/")
        self.assertIn(self.cs361, resp.context["courses"], msg="Not all courses displayed")
        self.assertIn(self.ee457, resp.context["courses"], msg="Not all courses displayed")

    def testViewSections(self):
        resp = self.monkey.get("/sections/")
        self.assertIn(self.cs361Lab, resp.context["sections"], msg="Not all sections displayed")
        self.assertIn(self.ee457Lec, resp.context["sections"], msg="Not all sections displayed")
