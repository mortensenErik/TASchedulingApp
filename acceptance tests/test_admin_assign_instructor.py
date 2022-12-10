from django.test import TestCase, Client
from app.models import UserProfile, Course, Section


class testAdminAssignInstructor(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', role="Instructor")
        self.miguel = UserProfile.objects.create(name='Miguel', id='miggy', password='ziggy', email='miggy@uwm.edu',
                                                phone='202-555-0191', address='abc120', role="TA")
        self.cs361 = Course.objects.create(CourseId='361', name='Intro to Software Engineering', number='CS361',
                                           subject="CompSci")
        self.cs361Lec = Section.objects.create(SectionId='401', type='LEC', course=self.cs361, faculty=None, number='361')
    def testAssignInstructor(self):
        self.monkey.get("/edit_section/", {"sectionNumber": "361-401", "teacher": "", "sectionType": "LEC"})
        self.monkey.post("/edit_section/", {"teacher": "bigboy@uwm.edu"})
        self.assertEqual(self.cs361Lec.teacher, self.nigel, msg="Instructor was not assigned to course")

    def testCourseAssignTa(self):
        self.monkey.get("/edit_section/", {"sectionNumber": "361-401", "teacher": "", "sectionType": "LEC"})
        self.monkey.post("/edit_section/", {"teacher": "miggy@uwm.edu"})
        self.assertEqual(self.cs361.instructor, None, msg="User cannot be assigned to this section")