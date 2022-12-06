from django.test import TestCase, Client
from app.models import UserProfile, Course, Section


class testAdminViewData(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', officeHours="Appointment Only",
                                                role="admin")
        self.cs361 = Course.objects.create(id='361', name='Intro to Software Engineering', number='CS361',
                                           instructor=self.nigel)
        self.cs361Lab = Section.objects.create(id='801', course=self.cs361, teacher=self.nigel, type='Lab')

    def testViewUsers(self):
        resp = self.monkey.get("/viewUsers/")
        self.assertIn(self.nigel, resp.context["users"], msg="Not all users displayed")

    def testViewCourses(self):
        resp = self.monkey.get("/viewCourses/")
        self.assertIn(self.cs361, resp.context["courses"], msg="Not all courses displayed")

    def testViewSections(self):
        resp = self.monkey.get("/viewSections/")
        self.assertIn(self.cs361Lab, resp.context["sections"], msg="Not all sections displayed")
