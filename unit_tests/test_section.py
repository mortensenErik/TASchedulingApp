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
        self.rock = UserProfile.objects.create(id="1", name="Jay Rock", password="pw", phone="414-555-5556",
                                               address="test",
                                               role="Instructor", email="rock@uwm.edu")
        self.sorenson = UserProfile.objects.create(id="21", name="Bob Sorenson", password="ps", phone="414-555-5557",
                                                   address="test1", role="TA", email="sorenson@uwm.edu")
        self.CS250 = Course.objects.create(CourseId="123", name="Introductory Computer Programming", number="250",
                                           subject="CS")
        self.CS400 = Section.objects.create(SectionId="12", course=self.CS250, faculty=self.rock, number="400",
                                            type="LEC")
        self.CS805 = Section.objects.create(SectionId="14", course=self.CS250, faculty=self.sorenson, number="805",
                                            type="LAB")

    def test_is_section_made(self):
        test = SectionClass.createSection(SectionId="13", course=self.CS250, faculty=self.sorenson, number="803",
                                          type="LAB")
        lookup = list(Section.objects.all())
        self.assertEqual(len(lookup), 3, msg="Error: unable to create section")

    def test_section_deleted(self):
        test = SectionClass.deleteSection(SectionId="14")
        lookup = list(Section.objects.all())
        self.assertEqual(len(lookup), 1, msg="Error: unable to delete section")

    def test_same_sectionId(self):
        test = SectionClass.createSection(SectionId="14", course=self.CS250, faculty=self.rock, number="809",
                                          type="LAB")
        lookup = list(Section.objects.all())
        self.assertEqual(len(lookup), 2, msg="Error: unable to create same sectionId")

    def test_same_number(self):
        test = SectionClass.createSection(SectionId="13", course=self.CS250, faculty=self.sorenson, number="805",
                                          type="LAB")
        lookup = list(Section.objects.all())
        self.assertEqual(len(lookup), 2, msg="Error: unable to create same number section")



class sectiontests(TestCase):
    def setUp(self):
        tempCourseforsec = Course.objects.create( name="data structures",number=351,subject="computer science")
        tempCourseforsec_lab = Section.objects.create(course=tempCourseforsec,number=801,type="LAB")
        tempCourseforsec_sec = Section.objects.create(course=tempCourseforsec,number=401,type="LEC")
        tempCourseforsec1 = Course.objects.create(name="system programimg", number=337,subject="Computer Science")
        tempCourseforsec1_sec = Section.objects.create(course=tempCourseforsec1,number=407,type="LEC")
        tempCourseforsec1_lab = Section.objects.create(course=tempCourseforsec1,number=409,type="LAB")




    def test_getsectionbyid_for_correct_info(self):
        okay = SectionClass.getSectionById(1)
        self.assertEqual(okay,Section.objects.get(number=801))


    def test_getsectionbyid_for_an_error_thing(self):
        with self.assertRaises(TypeError) as context:
            SectionClass.getSectionById()

    def test_getsectionbyid_for_an_Int_rite(self):
        okay = SectionClass.getSectionById(4)
        self.assertEqual(okay,Section.objects.get(number=409))

    def test_getsectionbyid_for_an_Int_rite2(self):
        okay = SectionClass.getSectionById(3)
        self.assertEqual(okay,Section.objects.get(number=407))

    def test_getsectionbyid_for_an_Int_rite3(self):
        okay = SectionClass.getSectionById(1)
        self.assertEqual(okay,Section.objects.get(number=801))

    def test_getsection_for_an_char_rite(self):
        okay2 = SectionClass.getSectionById('124')
        self.assertEqual(okay2,None)

    def test_vaild_literal(self):
        with self.assertRaises(ValueError) as context:
            SectionClass.getSectionById("5njfenjnf444")

class coursetests(TestCase):
    def setUp(self):
        tempCourseforcourse = Course.objects.create( name="data structures",number=351,subject="computer science")
        tempCourseforcourse1 = Course.objects.create( name="system programimg", number=337,subject="Computer Science")

    def test_getCoursebyid_for_correct_info(self):
        okay = CourseClass.getCourseById(2)
        self.assertTrue(okay,"Computer Science 337: system programimg")

    def test_getCoursebyid_for_correct_info2(self):
        okay = CourseClass.getCourseById(1)
        self.assertTrue(okay, "Computer Science 351: data structures")

    def test_getCourseid_for_an_Int_wrong(self):
        okay1 = CourseClass.getCourseById(123)
        self.assertEqual(okay1, None)

    def test_getCourseid_for_an_char_rite(self):
        okay2 = CourseClass.getCourseById('12346')
        self.assertEqual(okay2, None)

    def test_getCourseid_for_an_random_int_rite(self):
        okay2 = CourseClass.getCourseById(123876)
        self.assertEqual(okay2, None)

    def test_for_invalid_litaral(self):
        with self.assertRaises(ValueError) as context:
            SectionClass.getSectionById("8dsnjcjfsdnjs4s5v")

    def test_getCourseid_for_an_error_thing(self):
        with self.assertRaises(TypeError) as context:
            SectionClass.getSectionById()


class UserUnitTests(TestCase):
    def setUp(self):
        self.nigel = UserProfile.objects.create(name='Nigel',  password='boogy', email='bigboy@uwm.edu',
                                          phone='202-555-0196', role="INSTRUCTOR", address='chicago')
        self.jacey = UserProfile.objects.create(name='Jacey',  password='lmao', email='jacey@uwm.edu',
                                          phone='202-555-0168', role="TA",  address='miami')
        self.anna = UserProfile.objects.create(name='Annabelle',  password='hiyah', email='lechonk@uwm.edu',
                                         phone='202-555-0164', role="INSTRUCTOR", address='milwaukee')
        self.luke = UserProfile.objects.create(name='Luke',  password='kiki', email='bingbong@uwm.edu',
                                         phone='202-555-0157', role="ADMIN",  address='new york')
        self.edytha = UserProfile.objects.create(name='Edytha',  password='oof', email='edytha@uwm.edu',
                                           phone='202-555-0182', role="TA",  address='DC')


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
        self.nigel = UserProfile.objects.create(name='Nigel', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', role="INSTRUCTOR", address='chicago')
        self.jacey = UserProfile.objects.create(name='Jacey',  password='lmao', email='jacey@uwm.edu',
                                                phone='202-555-0168', role="TA", address='miami')
        self.anna = UserProfile.objects.create(name='Annabelle',  password='hiyah',
                                               email='lechonk@uwm.edu',
                                               phone='202-555-0164', role="INSTRUCTOR", address='milwaukee')
        self.luke = UserProfile.objects.create(name='Luke', password='kiki', email='bingbong@uwm.edu',
                                               phone='202-555-0157', role="ADMIN", address='new york')
        self.edytha = UserProfile.objects.create(name='Edytha',password='oof', email='edytha@uwm.edu',
                                                 phone='202-555-0182', role="TA", address='DC')


    def test_edit_noperson_found(self):
        with self.assertRaises(ValueError) as context:
            User.editProfileInfo('leck@uwm.edu', 'Annabelle', '202-555-0164', 'new jercy')

    def test_when_no_emailisgiven(self):
        with self.assertRaises(TypeError) as context:
            User.editProfileInfo('', 'Annabelle', '202-555-0164', 'new jercy')

    def test_changing_address(self):
        User.editProfileInfo('lechonk@uwm.edu', 'Annabelle', '202-555-0164', 'new jercy')
        self.assertEqual(User.getUserByEmail('lechonk@uwm.edu').address,'new jercy')

    def test_changing_phone_no(self):
        User.editProfileInfo('bingbong@uwm.edu', 'Luke', '202-555-7899', 'new york')
        self.assertEqual(User.getUserByEmail('bingbong@uwm.edu').phone,'202-555-7899')

    def test_changing_name(self):
        User.editProfileInfo('bingbong@uwm.edu', 'lakey', '202-555-7899', 'new york')
        self.assertEqual(User.getUserByEmail('bingbong@uwm.edu').name, 'lakey')

    def test_changing_2_ORmore_things(self):
        User.editProfileInfo('bingbong@uwm.edu', 'Luke', '202-999-7899', 'Los Angels')
        self.assertEqual(User.getUserByEmail('bingbong@uwm.edu').phone, '202-999-7899')
        self.assertEqual(User.getUserByEmail('bingbong@uwm.edu').address,  'Los Angels')

#if nothing is given while editing the database, everthing but that will be made to NULL
    def test_chaning_when_evrthing_but_email_is_gven(self):
        User.editProfileInfo('bingbong@uwm.edu', '', '', '')
        self.assertEqual(User.getUserByEmail('bingbong@uwm.edu').phone,  '')
        self.assertEqual(User.getUserByEmail('bingbong@uwm.edu').address,'')
        self.assertEqual(User.getUserByEmail('bingbong@uwm.edu').name,   '')

