from django.test import TestCase, Client
from app.models import UserProfile
from app.models import Course
from app.models import Section


class testDeleteCourse(TestCase):

    def setUp(self):
        self.thingy = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', role="admin")
        self.tempCourseforsec = Course.objects.create(name="data structures", number=351,
                                                      subject="computer science")
        self.tempCourseforsec_lab = Section.objects.create(course=self.tempCourseforsec, number=801, type="LAB")
        self.tempCourseforsec_sec = Section.objects.create(course=self.tempCourseforsec, number=401, type="LEC")
        self.tempCourseforsec1 = Course.objects.create(name="system programming", number=337,
                                                       subject="Computer Science")
        self.tempCourseforsec1_sec = Section.objects.create(course=self.tempCourseforsec1, number=407,
                                                            type="LEC")
        self.tempCourseforsec1_lab = Section.objects.create(course=self.tempCourseforsec1, number=409, type="LAB")

    def testDeleteCourse(self):
        self.thingy.session["email"] = self.nigel.email
        self.thingy.session["role"] = self.nigel.role
        self.thingy.get("/confirmDeleteCourse/" + str(self.tempCourseforsec1.CourseId) + "/")
        self.thingy.post("/courses/" + str(self.tempCourseforsec1.CourseId) + "/")
        self.assertEqual(len(Course.objects.filter(CourseId=self.tempCourseforsec1.CourseId)), 0,
                         msg="Course not deleted")
