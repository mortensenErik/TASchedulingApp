from django.test import TestCase, Client
from app.models import UserProfile

class testDeleteAccount(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', role="admin")
        self.frank = UserProfile.objects.create(name='Frank Furter', id='frankf', password='hotdog',
                                                email='frankf@uwm.edu', phone='202-555-0111', address='abc123',
                                                role="TA")

    def testDeleteAccount(self):
        self.monkey.get("/editProfile/", {"name": "Frank Furter", "password": "hotdog", "phone": "202-555-0111",
                                          "address": "abc123", "role": "TA",
                                          "email": "frankf@uwm.edu"})
        self.monkey.post("/editProfile/", {"delete": "on"})
        self.assertEqual(len(UserProfile.objects.filter(id="frankf")), 0, msg="User was not deleted")
