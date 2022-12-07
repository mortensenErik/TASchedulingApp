# import unittest
from app.models import TA, Instructor, Admin
from classes.AccountClass import createAccount, deleteAccount, editAccount

class testCreateAccount(unittest.TestCase):
    def setUp(self):
        self.nigel = Admin.objects.create(name='Nigel', id='bigboy', pw='boogy', email='bigboy@uwm.edu',
                                          phone='202-555-0196');
        self.jacey = Instructor.objects.create(name='Jacey', id='jacey', pw='lmao', email='jacey@uwm.edu',
                                               phone='202-555-0168')
        self.anna = TA.objects.create(name='Annabelle', id='lechonk', pw='hiyah', email='lechonk@uwm.edu',
                                      phone='202-555-0164')

    def testAccountExists(self):
        with self.assertRaises(ValueError, msg="createAccount fails to raise ValueError when an existing account is"
                                               " entered"):
            createAccount("bigboy@uwm.edu", "Admin")

    def testAccountDoesntExist(self):
        dave = createAccount("daveb@uwm.edu", "Admin")
        self.assertIn(dave, Admin.objects, msg="A new user was not added to the database")


class testDeleteAccount(unittest.TestCase):
    def setUp(self):
        self.nigel = Admin.objects.create(name='Nigel', id='bigboy', pw='boogy', email='bigboy@uwm.edu',
                                          phone='202-555-0196');
        self.jacey = Instructor.objects.create(name='Jacey', id='jacey', pw='lmao', email='jacey@uwm.edu',
                                               phone='202-555-0168')
        self.anna = TA.objects.create(name='Annabelle', id='lechonk', pw='hiyah', email='lechonk@uwm.edu',
                                      phone='202-555-0164')

    def testAccountExists(self):
        nigel = deleteAccount("bigboy@uwm.edu")
        self.assertNotIn(nigel, Admin.objects, msg="A user was not removed from the database")

    def testAccountDoesntExist(self):
        with self.assertRaises(ValueError, msg="deleteAccount fails to raise ValueError when a non-existing account is"
                                               " entered"):
            deleteAccount("daveb@uwm.edu")

class testEditAccount(unittest.TestCase):
    def setUp(self):
        self.nigel = Admin.objects.create(name='Nigel Anderson', id='bigboy', pw='boogy', email='bigboy@uwm.edu',
                                          phone='202-555-0196');
        self.jacey = Instructor.objects.create(name='Jacey', id='jacey', pw='lmao', email='jacey@uwm.edu',
                                               phone='202-555-0168')
        self.anna = TA.objects.create(name='Annabelle', id='lechonk', pw='hiyah', email='lechonk@uwm.edu',
                                      phone='202-555-0164')

    def testAccountExists(self):
        editAccount("bigboy@uwm.edu", {"name": "Nigel Orerson", "email": "smallboy@uwm.edu", "phone": "414-555-6776"})
        self.assertEqual(self.nigel.name, "Nigel Orerson", msg="editAccount failed to change name")
        self.assertEqual(self.nigel.id, "smallboy", msg="editAccount failed to change id")
        self.assertEqual(self.nigel.pw, "boogy", msg="editAccount changed password")
        self.assertEqual(self.nigel.email, "smallboy@uwm.edu", msg="editAccount failed to change email")
        self.assertEqual(self.nigel.phone, "414-555-6776", msg="editAccount failed to change phone number")

    def testAccountDoesntExist(self):
        with self.assertRaises(ValueError, msg="editAccount fails to raise ValueError when a non-existing account is"
                                               " entered"):
            editAccount("daveb@uwm.edu", {"phone":"414-555-6776"})
