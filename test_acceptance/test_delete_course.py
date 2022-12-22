from django.test import TestCase, Client
from app.models import UserProfile
from app.models import Course
from app.models import Section


class testDeleteSection(TestCase):
    def setUp(self):
        self.thingy = Client()
        self.rock = UserProfile.objects.create(name="Jay Rock", password="pw", phone="414-555-5556",
                                               address="test",
                                               role="Instructor", email="rock@uwm.edu")
        self.sorenson = UserProfile.objects.create(name="Bob Sorenson", password="ps", phone="414-555-5557",
                                                   address="test1", role="TA", email="sorenson@uwm.edu")
        self.CS250 = Course.objects.create(name="Introductory Computer Programming", number="250",
                                           subject="CS")
        self.CS400 = Section.objects.create(course=self.CS250, faculty=self.rock, number="400",
                                            type="LEC")
        self.CS805 = Section.objects.create(course=self.CS250, faculty=self.sorenson, number="805",
                                            type="LAB")
        self.CS251 = Course.objects.create(name="intermediate Computer Programming", number="251",
                                           subject="CS")
    def testDeleteCourse(self):
        self.thingy.session["number"] = self.CS250.number
        self.thingy.session["subject"]   = self.CS250.subject
        self.thingy.get("/confirmDeleteCourse/" + str(self.CS251.CourseId) + "/")
        self.thingy.post("/Course/CS805/")
        self.assertEqual(len(Section.objects.filter(course_id=self.CS251.CourseId)), 0 , msg="course not deleted")

