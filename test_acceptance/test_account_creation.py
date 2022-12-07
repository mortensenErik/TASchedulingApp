from django.test import TestCase, Client
from app.models import UserProfile


class testCreateUser(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', officeHours="Appointment Only",
                                                role="admin")

    def testCreateNewUser(self):
        resp = self.monkey.post("/createUser/", {"email": "shaqon@uwm.edu", "name": "Shaquille O'Neal",
                                                 "password": "basketball", "role": "admin", "phone": "yes",
                                                 "address": "EMS E250", "officeHours": "M 9:00am-11:30am"})
        self.assertEqual(len(UserProfile.objects.filter(id="shaqon")), 1, msg="User was not created")

    def testCreateOldUser(self):
        resp = self.monkey.post("/createUser/", {"email": "bigboy@uwm.edu", "name": "Shaquille O'Neal",
                                                 "password": "basketball", "role": "admin", "phone": "yes",
                                                 "address": "EMS E250", "officeHours": "M 9:00am-11:30am"})
        self.assertEqual(len(UserProfile.objects.filter(id="bigboy")), 1, msg="Multiple users with the same id exist")
        self.assertEqual(len(UserProfile.objects.filter(id="bigboy", name="Nigel")), 1,
                         msg="An existing user's data was overwritten")
