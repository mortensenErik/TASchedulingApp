from django.test import TestCase, Client
from app.models import UserProfile


class testCreateUser(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', role="Admin")

    def testCreateNewUser(self):
        resp = self.monkey.post("/new_user/", {"email": "shaqon@uwm.edu", "name": "Shaquille O'Neal",
                                               "password": "basketball", "role": "Admin", "phone": "yes",
                                               "address": "EMS E250"})
        self.assertEqual(len(UserProfile.objects.filter(email="shaqon@uwm.edu")), 1, msg="User was not created")

    def testCreateOldUser(self):
        resp = self.monkey.post("/new_user/", {"email": "bigboy@uwm.edu", "name": "Shaquille O'Neal",
                                               "password": "basketball", "role": "Admin", "phone": "yes",
                                               "address": "EMS E250"})
        self.assertEqual(len(UserProfile.objects.filter(email="bigboy@uwm.edu")), 1, msg="Multiple users with the same"
                                                                                         " email exist")
        self.assertEqual(len(UserProfile.objects.filter(email="bigboy@uwm.edu", name="Nigel")), 1,
                         msg="An existing user's data was overwritten")
