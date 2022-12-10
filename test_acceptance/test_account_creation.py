from django.test import TestCase, Client
from app.models import UserProfile


class testCreateUser(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', role="Admin")

    def testCreateNewUser(self):
        resp = self.monkey.post("/new_user/", {"id": "shaqon", "email": "shaqon@uwm.edu", "name": "Shaquille O'Neal",
                                               "password": "basketball", "role": "Admin", "phone": "yes",
                                               "address": "EMS E250"})
        self.assertEqual(len(UserProfile.objects.filter(id="shaqon")), 1, msg="User was not created")

    def testCreateOldUser(self):
        resp = self.monkey.post("/new_user/", {"id": "bigboy", "email": "bigboy@uwm.edu", "name": "Shaquille O'Neal",
                                               "password": "basketball", "role": "Admin", "phone": "yes",
                                               "address": "EMS E250"})
        self.assertEqual(len(UserProfile.objects.filter(id="bigboy")), 1, msg="Multiple users with the same id exist")
        self.assertEqual(len(UserProfile.objects.filter(id="bigboy", name="Nigel")), 1,
                         msg="An existing user's data was overwritten")
