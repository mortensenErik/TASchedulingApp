from django.test import TestCase, Client
from app.models import UserProfile
from app.models import Course
from app.models import Section


class testDeleteSection(TestCase):

    def setUp(self):
        self.thingy = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', role="admin")
        self.tempCourseforsec = Course.objects.create(name="data structures", number=351,
                                                      subject="computer science")
        self.tempCourseforsec_lab = Section.objects.create(course=self.tempCourseforsec, number=801, type="LAB")
        self.tempCourseforsec_sec = Section.objects.create(course=self.tempCourseforsec, number=401, type="LEC")
        self.tempCourseforsec1 = Course.objects.create(name="system programming", number=337,
                                                       subject="Computer Science")
        self.tempCourseforsec1_sec = Section.objects.create(course=self.tempCourseforsec1, number=407,
                                                            type="LEC")
        self.tempCourseforsec1_lab = Section.objects.create(course=self.tempCourseforsec1, number=409, type="LAB")

    def testDeleteSections(self):
        self.thingy.session["email"] = self.nigel.email
        self.thingy.session["role"] = self.nigel.role
        self.thingy.get("/confirmDeleteSection/" + str(self.tempCourseforsec1_sec.SectionId) + "/")
        self.thingy.post("/sections/" + str(self.tempCourseforsec1_sec.SectionId) + "/")
        self.assertEqual(len(Section.objects.filter(SectionId=self.tempCourseforsec1_sec.SectionId)), 0,
                         msg="Section not deleted")
