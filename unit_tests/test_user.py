from django.test import TestCase

from app.models import UserProfile


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

    def test_list_user_email(self):
        admin_list = UserProfile.objects.filter(email='bingbong@umw.edu')
        self.assertEqual(len(admin_list), 1)
        test = UserProfile.objects.filter(email='test@uwm.edu')
        self.assertEqual(len(test), 0)

    def test_list_user_names(self):
        admin_list = list(UserProfile.objects.filter(name='Nigel'))
        self.assertEqual(len(admin_list), 1)

    def test_edit_phone(self):
        self.nigel.phone = '321-012-3456'
        self.assertEqual(self.nigel.phone, '321-012-3456')

    def test_pw(self):
        admin_list = UserProfile.objects.filter(password='oof')
        self.assertEqual(len(admin_list), 1)
        test = UserProfile.objects.filter(password='')
        self.assertEqual(len(test), 0)

    def test_delete(self):
        self.nigel.delete()
        lookup = UserProfile.objects.all()
        self.assertEqual(len(lookup), 4, msg="Error: user was not deleted")
        admin_list = list(UserProfile.objects.filter(name='Nigel'))
        self.assertEqual(len(admin_list), 0)
        
    def test_create_user(self):
        test = User.createUser(id="lks", name="Jerry", password="none", phone="414-555-5555", address="test", role="TA",
                               email="jerr@uwm.edu")
        lookup = UserProfile.objects.all()
        self.assertEqual(len(lookup), 6, msg="Error: unable to delete user")
        
    def test_delete_user(self):
        test = User.deleteUser(email="bigboy@uwm.edu")
        lookup = UserProfile.objects.all()
        self.assertEqual(len(lookup), 4, msg="Error: unable to delete user")
