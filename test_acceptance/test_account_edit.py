from django.test import TestCase, Client
from app.models import UserProfile


class testEditAccount(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.paul = UserProfile.objects.create(name='Paul', password='dietcoke', email='paulie@uwm.edu',
                                               phone='202-555-0198', address='abc129', role="Instructor")

    def testEditAccount(self):
        self.monkey.get("/edit_user/" + str(self.paul.id) + "/")
        self.monkey.post("/edit_user/" + str(self.paul.id) + "/", {"email": "paulie@uwm.edu", "name": "Paul",
                                                                   "password": "dietcoke", "role": "Instructor",
                                                                   "phone": "yes", "address": "123abc"})
        self.assertEqual(UserProfile.objects.get(name="Paul").address, "123abc", msg="Account not updated")
