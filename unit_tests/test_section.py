from django.test import TestCase
#
from app.models import Section
from app.models import Course
from app.models import UserProfile
from classes import SectionClass
from classes.SectionClass import *

class CreateSectionTest(TestCase):
    def setUp(self):
        self.rock = UserProfile.objects.create(id="1", name="Jay Rock", password="pw", phone="414-555-5556", address="test",
                                              role="Instructor", email="rock@uwm.edu")
        self.sorenson = UserProfile.objects.create(id="21", name="Bob Sorenson", password="ps", phone="414-555-5557",
                                                   address="test1", role="TA", email="sorenson@uwm.edu")
        self.CS250 = Course.objects.create(CourseId="123", name="Introductory Computer Programming", number="250", subject="CS")
        self.CS400 = Section.objects.create(SectionId="12", course=self.CS250, faculty=self.rock, number="400", type="LEC")
        self.CS805 = Section.objects.create(SectionId="14", course=self.CS250, faculty=self.sorenson, number="805", type="LAB")

    def test_is_section_made(self):
        test = SectionClass.createSection(SectionId="13", course=self.CS250, faculty=self.sorenson, number="803", type="LAB")
        lookup = list(Section.objects.all())
        self.assertEqual(len(lookup), 3, msg="Error: unable to create section")

    def test_section_deleted(self):
        test = SectionClass.deleteSection(SectionId="14")
        lookup = list(Section.objects.all())
        self.assertEqual(len(lookup), 1, msg="Error: unable to delete section")
        
    def test_same_sectionId(self):
        test = SectionClass.createSection(SectionId="14", course=self.CS250, faculty=self.rock, number="809", type="LAB")
        lookup = list(Section.objects.all())
        self.assertEqual(len(lookup), 2, msg="Error: unable to create same sectionId")
        
    def test_same_number(self):
        test = SectionClass.createSection(SectionId="13", course=self.CS250, faculty=self.sorenson, number="805", type="LAB")
        lookup = list(Section.objects.all())
        self.assertEqual(len(lookup), 2, msg="Error: unable to create same number section")
