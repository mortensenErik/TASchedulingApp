from django.test import TestCase

from app.models import UserProfile


class UserUnitTests(TestCase):
    def setUp(self):
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', pw='boogy', email='bigboy@uwm.edu',
                                          phone='202-555-0196')
        self.jacey = UserProfile.objects.create(name='Jacey', id='jacey', pw='lmao', email='jacey@uwm.edu',
                                          phone='202-555-0168')
        self.anna = UserProfile.objects.create(name='Annabelle', id='lechonk', pw='hiyah', email='lechonk@uwm.edu',
                                         phone='202-555-0164')
        self.luke = UserProfile.objects.create(name='Luke', id='bingbong', pw='kiki', email='bingbong@uwm.edu',
                                         phone='202-555-0157')
        self.edytha = UserProfile.objects.create(name='Edytha', id='edytha', pw='oof', email='edytha@uwm.edu',
                                           phone='202-555-0182')

    def test_list_user_length(self):
        admin_list = UserProfile.objects.filter(len(UserProfile.id) > 3)
        self.assertEqual(len(admin_list), 5)

    def test_list_user_names(self):
        admin_list = list(UserProfile.objects.filter(name='Nigel'))
        self.assertEqual(len(admin_list), 1)

    def test_edit_phone(self):
        self.nigel.phone = '321-012-3456'
        self.assertEqual(self.nigel.phone, '321-012-3456')

    def test_pw(self):
        admin_list = list(UserProfile.objects.filter(len(UserProfile.pw) > 4))
        self.assertEqual(len(admin_list), 2)

    def test_delete(self):
        self.nigel.delete()
        self.assertEqual(len(list(UserProfile.objects), 4))
        admin_list = list(UserProfile.objects.filter(name='Nigel'))
        self.assertEqual(len(admin_list), 0)
        
    def test_create_user(self):
        test = UserProfile.objects.create(id="tryin", name="Jerry", password="none", phone="414-555-5555", address="test",
                                          role="TA", email="jerr@uwm.edu")
        lookup = list(UserProfile.objects.all())
        self.assertEqual(len(lookup), 5, msg="Error: unable to create user")
