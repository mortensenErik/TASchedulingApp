from django.test import TestCase
from app.models import Section
from app.models import Course
from app.models import UserProfile
from classes import SectionClass
from classes.SectionClass import *
from app.models import Course, Section, UserProfile
from classes import SectionClass, CourseClass
from classes.SectionClass import SectionClass
from classes.CourseClass import CourseClass
from classes.UserClass import User


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



class sectiontests(TestCase):
    def setUp(self):
        tempCourseforsec = Course.objects.create(CourseId="12345", name="data structures",number=351,subject="computer science")
        tempCourseforsec_lab = Section.objects.create(SectionId="123",course=tempCourseforsec,number=801,type="LAB")
        tempCourseforsec_sec = Section.objects.create(SectionId="124",course=tempCourseforsec,number=401,type="LEC")
        tempCourseforsec1 = Course.objects.create(CourseId="12346", name="system programimg", number=337,subject="Computer Science")
        tempCourseforsec1_sec = Section.objects.create(SectionId="125",course=tempCourseforsec1,number=407,type="LEC")
        tempCourseforsec1_lab = Section.objects.create(SectionId="126",course=tempCourseforsec1,number=409,type="LAB")




    def test_getsectionbyid_for_correct_info(self):
        okay = SectionClass.getSectionById("124")
        self.assertEqual(okay,Section.objects.get(SectionId="124"))


    def test_getsectionbyid_for_an_error_thing(self):
        with self.assertRaises(TypeError) as context:
            SectionClass.getSectionById()

    def test_getsectionbyid_for_an_Int_rite(self):
        okay = SectionClass.getSectionById(124)
        self.assertEqual(okay,Section.objects.get(SectionId="124"))

    def test_getsection_for_an_char_rite(self):
        okay2 = SectionClass.getSectionById('124')
        self.assertEqual(okay2,Section.objects.get(SectionId="124"))

    def test_getsection_for_an_randomwrong(self):
        okay2 = SectionClass.getSectionById("5njfenjnf444")
        self.assertEqual(okay2,None)


class coursetests(TestCase):
    def setUp(self):
        tempCourseforcourse = Course.objects.create(CourseId="12345", name="data structures",number=351,subject="computer science")
        tempCourseforcourse1 = Course.objects.create(CourseId="12346", name="system programimg", number=337,subject="Computer Science")



    def test_getCoursebyid_for_correct_info(self):
        okay = CourseClass.getCourseById("12346")
        self.assertTrue(okay,"Computer Science 337: system programimg")

    def test_getCourseid_for_an_Int_wrong(self):
        okay1 = CourseClass.getCourseById(123)
        self.assertEqual(okay1, None)

    def test_getCourseid_for_an_char_rite(self):
        okay2 = CourseClass.getCourseById('12346')
        self.assertEqual(okay2, Course.objects.get(CourseId="12346"))

    def test_getCourseid_for_an_int_rite(self):
        okay2 = CourseClass.getCourseById(12346)
        self.assertEqual(okay2, Course.objects.get(CourseId="12346"))

    def test_getCourseid_for_an_random_wrong(self):
        okay3 = CourseClass.getCourseById("845g45e")
        self.assertEqual(okay3,None)

    def test_getCourseid_for_an_error_thing(self):
        with self.assertRaises(TypeError) as context:
            SectionClass.getSectionById()


class UserUnitTests(TestCase):
    def setUp(self):
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', password='boogy', email='bigboy@uwm.edu',
                                          phone='202-555-0196', role="INSTRUCTOR")
        self.jacey = UserProfile.objects.create(name='Jacey', id='jacey', password='lmao', email='jacey@uwm.edu',
                                          phone='202-555-0168', role="TA")
        self.anna = UserProfile.objects.create(name='Annabelle', id='lechonk', password='hiyah', email='lechonk@uwm.edu',
                                         phone='202-555-0164', role="INSTRUCTOR")
        self.luke = UserProfile.objects.create(name='Luke', id='bingbong', password='kiki', email='bingbong@uwm.edu',
                                         phone='202-555-0157', role="ADMIN")
        self.edytha = UserProfile.objects.create(name='Edytha', id='edytha', password='oof', email='edytha@uwm.edu',
                                           phone='202-555-0182', role="TA")


    def test_getuserbyemail(self):
        okay1 = User.getUserByEmail("bigboy@uwm.edu")
        self.assertEqual(okay1,UserProfile.objects.get(email="bigboy@uwm.edu"))

    def test_getuserbyemail_oneqote(self):
        okay2 = User.getUserByEmail('lechonk@uwm.edu')
        self.assertEqual(okay2,UserProfile.objects.get(email="lechonk@uwm.edu"))

    def test_getuserbyemail_wrong(self):
        okay3 = User.getUserByEmail('kjefejfk0@uwm.edu')
        self.assertEqual(okay3,None)

    def test_getuserbyemail_wrongtype(self):
        okay4 = User.getUserByEmail(45475)
        self.assertEqual(okay4,None)

    def test_getuserbyemail_ERROR(self):
        with self.assertRaises(TypeError) as context:
            User.getUserByEmail()

class Useredittest(TestCase):

    def setUp(self):
        pass


    def test_editedthing(self):
        pass
