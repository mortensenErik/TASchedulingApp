from django.test import TestCase
from app.models import *
from .models import UserProfile

# Create your unit_tests here.


class AdmitUnitTests(TestCase):
    def setUp(self):
        self.nigel = Admin.objects.create(name='Nigel', id='bigboy', pw = 'boogy', email='bigboy@uwm.edu', phone='202-555-0196')
        self.jacey = Admin.objects.create(name='Jacey', id='jacey', pw= 'lmao', email='jacey@uwm.edu', phone='202-555-0168')
        self.anna = Admin.objects.create(name='Annabelle', id='lechonk', pw = 'hiyah', email='lechonk@uwm.edu', phone='202-555-0164')
        self.luke = Admin.objects.create(name='Luke', id='bingbong', pw = 'kiki',  email='bingbong@uwm.edu', phone='202-555-0157')
        self.edytha = Admin.objects.create(name='Edytha', id= 'edytha', pw = 'oof', email='edytha@uwm.edu', phone='202-555-0182')

    def test_list_admin_length(self):
        admin_list = Admin.objects.filter(len(Admin.id) > 3)
        self.assertEqual(len(admin_list), 5)

    def test_list_admin_names(self):
        admin_list = list(Admin.objects.filter(name ='Nigel'))
        self.assertEqual(len(admin_list),1)

    def test_edit_phone(self):
        self.nigel.phone = '321-012-3456'
        self.assertEqual(self.nigel.phone, '321-012-3456')

    def test_pw(self):
        admin_list = list(Admin.objects.filter(len(Admin.pw) > 4))
        self.assertEqual(len(admin_list), 2)

    def test_delete_cardiologist(self):
        self.nigel.delete()
        self.assertEqual(len(list(Admin.objects), 4))
        admin_list = list(Admin.objects.filter(name='Nigel'))
        self.assertEqual(len(admin_list), 0)


class InstructorTest(TestCase):
    def setUp(self):
        self.shawn = Instructor.objects.create(id='shawn3', password='admin', name='Shawn', phone='920-555-5555', address='EMS 400',
                                               email='testshawn@uwm.edu')
        self.haitam = Instructor.objects.create(id='haitam6', password='admin1', name='Haitam', phone='920-555-5556', address='EMS 401',
                                                email="testhaitam@uwm.edu")
        self.erik = Instructor.objects.create(id='erik2', password='admin2', name='Erik', phone='920-555-5557', adress='EMS 402',
                                              email='testerik@uwm.edu')
        self.phani = Instructor.objects.create(id='phani1', password='admin3', name='Phani', phone='920-555-5558', address='EMS 403',
                                               email='testphani@uwm.edu')

    def test_instructor_names(self):
        instructor_name_list = list(Instructor.objects.filter(name=''))
        self.assertEqual(instructor_name_list, [self.shawn, self.haitam, self.erik, self.phani])

    def test_instructor_ids(self):
        instructor_id_list = list(Instructor.objects.filter(id=''))
        self.assertEqual(instructor_id_list, [self.shawn, self.haitam, self.erik, self.phani])

    def test_instructor_phone(self):
        instructor_phone_list = list(Instructor.object.filter(phone=''))
        self.assertEqual(instructor_phone_list, [self.shawn, self.haitam, self.erik, self.phani])

    def test_instructor_address(self):
        instructor_address_list = list(Instructor.object.filter(address=''))
        self.assertEqual(instructor_address_list, [self.shawn, self.haitam, self.erik, self.phani])

    def test_instructor_email(self):
        instructor_email_list = list(Instructor.object.filter(email=''))
        self.assertEqual(instructor_email_list, [self.shawn, self.haitam, self.erik, self.phani])

    def test_instructor_password(self):
        instructor_password_list = list(Instructor.object.filter(password=''))
        self.assertEqual(instructor_password_list, [self.shawn, self.haitam, self.erik, self.phani])

class OfficeHoursTest(TestCase):
    def setUp(self):
        self.lei = ta.object.create(id= lyao, password = ta123, name = 'Lei', phone = '555-555-5555', address='EMS101',
                                    email='lyao@uwm.edu', hours = '')

    def test_set_hours(self):
        self.lei.hours = 'M 2:00-3:30, W 2:00-3:30'
        self.assertEqual(self.lei.hours, 'M 2:00-3:30, W 2:00-3:30')

    def test_delete_hours(self):
        self.lei.hours = ''
        self.assertEqual(self.lei.hours, '')

    def test_hours_limit(self):
        self.lei.hours = 'T R 9:30-10:30, F 10:00-12:00 and only these words shouldn’t appear'
        self.assertEqual(self.lei.hours, 'T R 9:30-10:30, F 10:00-12:00 ')

