from django.test import TestCase

from app.models import Course
from app.models import Section
from app.models import UserProfile
from classes import SectionClass
from classes.SectionClass import SectionClass
from classes.CourseClass import CourseClass
from classes.UserClass import User




class sectiontests(TestCase):
    def setUp(self):
        tempCourseforsec = Course.objects.create(CourseId="12345", name="data structures",number=351,subject="computer science")
        tempCourseforsec_lab = Section.objects.create(SectionId="123",course=tempCourseforsec,number=801,type="LAB")
        tempCourseforsec_sec = Section.objects.create(SectionId="124",course=tempCourseforsec,number=401,type="LEC")
        tempCourseforsec1 = Course.objects.create(CourseId="12346", name="system programimg", number=337,subject="Computer Science")
        tempCourseforsec1_sec = Section.objects.create(SectionId="125",course=tempCourseforsec1,number=401,type="LEC")
        tempCourseforsec1_lab = Section.objects.create(SectionId="126",course=tempCourseforsec1,number=401,type="LAB")




    def test_get_section_by_id(self):
        okay = SectionClass.getSectionById("124")
        self.assertEqual(okay,Section.objects.filter(SectionId="123"))
        okay1 = SectionClass.getSectionById("123")
        # self.assertEqual()
        with self.assertRaises(TypeError) as context:
            SectionClass.getSectionById(123)




class coursetests(TestCase):
    def setUp(self):
        tempCourseforcourse = Course.objects.create(CourseId="12345", name="data structures",number=351,subject="computer science")
        tempCourseforcourse1 = Course.objects.create(CourseId="12346", name="system programimg", number=337,subject="Computer Science")



    def test_getCoursebyid(self):
        okay = CourseClass.getCourseById("12346")
        self.assertTrue(okay,"Computer Science 337: system programimg")
        with self.assertRaises(TypeError) as context:
            CourseClass.getCourseById(123)


