from django.test import TestCase
#
from app.models import Section
from app.models import Course
from app.models import UserProfile
from classes import SectionClass
from classes.SectionClass import *

class CreateSectionTest(TestCase):
    def setUp(self):
        self.rock = UserProfile.objects.create(id="12", name="Jay Rock", password="pw", phone = "test", address="tst" , role ="Instructor", email="test@uwm.edu")
        self.CS351 = Course.objects.create(CourseId="122", name="Data Structures and Algorithms", number="351", subject="CS")
        self.CS801 = Section.objects.create(SectionId="1", course=self.CS351, faculty=self.rock, number="801", type="LEC")

    def test_is_section_made(self):
        test = SectionClass.createSection(SectionId="13", course=self.CS351, faculty=self.rock, number="805", type="LAB")
        lookup = list(Section.objects.all())
        self.assertEqual(len(lookup), 2, msg="Error: unable to create section")
        
    def test_section_delete(self):
        test = SectionClass.deleteSection(SectionId="13", course=self.CS351, faculty=self.rock, number="805", type="LAB")
        lookup = list(Section.objects.all())
        self.assertEqual(len(lookup), 1, msg="Error: unable to delete section")


    #def test_data_is_not_right(self):
    #    okay =  make_section({{"id": 5454}, {"number": 801}, {"type": "lab"}})
    #    self.assertFalse(okay,msg="Error: course was made even with a bad id")
    #    lookfor= list(Section.objects.filter(course_name="compsci",number=351))
    #    self.assertEqual(len(lookfor),0,msg="Error: a course was made when course doesn't exist")
