from django.test import TestCase, Client
from app.models import UserProfile

class testEditSelf(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', role="admin")
        self.frank = UserProfile.objects.create(name='Frank Furter', id='frankf', password='hotdog',
                                                email='frankf@uwm.edu', phone='202-555-0111', address='abc123',
                                                role="TA")
        self.hank = UserProfile.objects.create(name='Hank Henderson', id='hankh', password='password123',
                                               email='hankh@uwm.edu', phone='212-555-0341', address='abc123',
                                               role="Instructor")

    def testEditSelfAdmin(self):
        self.monkey.post("", {"email": "bigboy@uwm.edu", "password": "boogy"})
        self.monkey.post("/edit_profile/", {"email": "bigboy@uwm.edu", "name": "Nigel New", "phone": "7777777777",
                                            "address": "abc123"})
        self.assertEqual(UserProfile.objects.filter(email="bigboy@uwm.edu").first().email, "bigboy@uwm.edu",
                         msg="Email was updated")
        self.assertEqual(UserProfile.objects.filter(email="bigboy@uwm.edu").first().address, "abc123",
                         msg="Address was updated")
        self.assertEqual(UserProfile.objects.filter(email="bigboy@uwm.edu").first().name, "Nigel New",
                         msg="Name was not updated")
        self.assertEqual(UserProfile.objects.filter(email="bigboy@uwm.edu").first().phone, "7777777777",
                         msg="Phone was not updated")

    def testEditSelfTA(self):
        self.monkey.post("", {"email": "frankf@uwm.edu", "password": "hotdog"})
        self.monkey.post("/edit_profile/", {"email": "frankf@uwm.edu", "name": "Frankenstein", "phone": "8989991234",
                                            "address": "abc123"})
        self.assertEqual(UserProfile.objects.filter(email="frankf@uwm.edu").first().email, "frankf@uwm.edu",
                         msg="Email was updated")
        self.assertEqual(UserProfile.objects.filter(email="frankf@uwm.edu").first().address, "abc123",
                         msg="Address was updated")
        self.assertEqual(UserProfile.objects.filter(email="frankf@uwm.edu").first().name, "Frankenstein",
                         msg="Name was not updated")
        self.assertEqual(UserProfile.objects.filter(email="frankf@uwm.edu").first().phone, "8989991234",
                         msg="Phone was not updated")

    def testEditSelfInstructor(self):
        self.monkey.post("", {"email": "hankh@uwm.edu", "password": "password123"})
        self.monkey.post("/edit_profile/", {"email": "hankh@uwm.edu", "name": "Just Hank", "phone": "4598889898",
                                            "address": "abc123"})
        self.assertEqual(UserProfile.objects.filter(email="hankh@uwm.edu").first().email, "hankh@uwm.edu",
                         msg="Email was updated")
        self.assertEqual(UserProfile.objects.filter(email="hankh@uwm.edu").first().address, "abc123",
                         msg="Address was updated")
        self.assertEqual(UserProfile.objects.filter(email="hankh@uwm.edu").first().name, "Just Hank",
                         msg="Name was not updated")
        self.assertEqual(UserProfile.objects.filter(email="hankh@uwm.edu").first().phone, "4598889898",
                         msg="Phone was not updated")
