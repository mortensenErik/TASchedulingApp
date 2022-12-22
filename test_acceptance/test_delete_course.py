from django.test import TestCase, Client
from app.models import UserProfile
from app.models import Course
from app.models import Section


class testDeleteSection(TestCase):
    def setUp(self):
        self.thingy = Client()
        tempCourseforsec = Course.objects.create(CourseId="12345", name="data structures", number=351,
                                                 subject="computer science")
        tempCourseforsec_lab = Section.objects.create(SectionId="123", course=tempCourseforsec, number=801, type="LAB")
        tempCourseforsec_sec = Section.objects.create(SectionId="124", course=tempCourseforsec, number=401, type="LEC")
        tempCourseforsec1 = Course.objects.create(CourseId="12346", name="system programimg", number=337,
                                                  subject="Computer Science")
        tempCourseforsec1_sec = Section.objects.create(SectionId="125", course=tempCourseforsec1, number=407,
                                                       type="LEC")
        tempCourseforsec1_lab = Section.objects.create(SectionId="126", course=tempCourseforsec1, number=409,
                                                       type="LAB")

    def testDeleteSections(self):
        resp = self.thingy.post("delete_section")
