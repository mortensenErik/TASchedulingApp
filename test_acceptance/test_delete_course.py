from django.test import TestCase, Client
from app.models import UserProfile
from app.models import Course
from app.models import Section


class testDeleteSection(TestCase):
    def setUp(self):
        self.thingy = Client()
        tempCourseforsec = Course.objects.create( name="data structures", number=351,
                                                 subject="computer science")
        tempCourseforsec_lab = Section.objects.create( course=tempCourseforsec, number=801, type="LAB")
        tempCourseforsec_sec = Section.objects.create(course=tempCourseforsec, number=401, type="LEC")
        tempCourseforsec1 = Course.objects.create( name="system programimg", number=337,
                                                  subject="Computer Science")
        tempCourseforsec1_sec = Section.objects.create( course=tempCourseforsec1, number=407,
                                                       type="LEC")
        tempCourseforsec1_lab = Section.objects.create( course=tempCourseforsec1, number=409,
                                                       type="LAB")

     def testDeleteSections(self):
        self.thingy.session["number"] = self.CS250.number
        self.thingy.session["subject"]   = self.CS250.subject
        self.thingy.get("/confirmDeleteCourse/" + str(self.CS251.CourseId) + "/")
        self.thingy.post("/Course/CS805/")
        self.assertEqual(len(Section.objects.filter(course_id=self.CS251.CourseId)), 0 , msg="course not deleted")


