from django.test import TestCase
#
from app.models import Section
from app.models import Course
from app.models import UserProfile
from classes import SectionClass
from classes.SectionClass import make_section

class CreateSectionTest(TestCase):
    def setUp(self):
        self.rock = UserProfile.objects.create(name="Jay Rock", id = "12", email="fs", phone = 'test', officeHours = 'test', role ='test')
        self.tempCourse = Course.objects.create(name="compsci", number="351",
                                 id="1253", instructor = self.rock)
        self.tempCourse.save()

    def test_is_section_made(self):
        okay = make_section({{"id": "12350"}, {"number": 801}, {"type": "lab"}})
        self.assertTrue(okay, msg="Error: creating a section for a course that exists")
        lookfor = list(Section.objects.filter(course_name="compsci",number="351"))
        self.assertEqual(len(lookfor), 1, msg="Error: not even a single section is created for the course")
        self.assertEqual(lookfor[0].number,801,"Error: the section that was inteded is not what was created")


    def test_data_is_not_right(self):
        okay =  make_section({{"id": 5454}, {"number": 801}, {"type": "lab"}})
        self.assertFalse(okay,msg="Error: course was made even with a bad id")
        lookfor= list(Section.objects.filter(course_name="compsci",number=351))
        self.assertEqual(len(lookfor),0,msg="Error: a course was made when course doesn't exist")
