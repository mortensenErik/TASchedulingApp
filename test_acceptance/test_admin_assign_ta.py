from django.test import TestCase, Client
from app.models import UserProfile, Course, Section


class testAdminAssignTA(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', role="admin")
        self.frank = UserProfile.objects.create(name='Frank Furter', password='hotdog',
                                                email='frankf@uwm.edu', phone='202-555-0111',
                                                address='abc123', role="TA")
        self.cs361 = Course.objects.create(name='Intro to Software Engineering', number='361',
                                           subject="COMPSCI")
        self.cs361Lab = Section.objects.create(type='LAB', course=self.cs361, faculty=None,
                                               number="801")

    def testAssignTA(self):
        self.monkey.get("/edit_section/" + str(self.cs361Lab.SectionId) + "/")
        self.monkey.post("/edit_section/" + str(self.cs361Lab.SectionId) + "/", {"number": self.cs361Lab.number,
                                                                                 "faculty": self.frank.id,
                                                                                 "type": self.cs361Lab.type})
        self.assertEqual(Section.objects.filter(SectionId=self.cs361Lab.SectionId).first().faculty, self.frank,
                         msg="TA not assigned to course")
