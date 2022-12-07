from django.test import TestCase, Client
from app.models import UserProfile, Course, Section


class testAdminAssignInstructor(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', officeHours="Appointment Only",
                                                role="Instructor")
        self.miguel = UserProfile.objects.create(name='Miguel', id='miggy', password='ziggy', email='miggy@uwm.edu',
                                                phone='202-555-0190', address='abc120', officeHours="Always",
                                                role="TA")
        self.cs361 = Course.objects.create(id='361', name='Intro to Software Engineering', number='CS361',
                                           instructor=None)
        self.cs361Lec = Section.objects.create(id='401', type='LEC', course=self.cs361, teacher=None)
    def testAssignInstructor(self):
        self.monkey.get("/edit_section/", {"sectionNumber": "361-401", "teacher": "", "sectionType": "LEC"})
        self.monkey.post("/edit_section/", {"teacher": "bigboy@uwm.edu"})
        self.assertEqual(self.cs361Lec.teacher, self.nigel, msg="Instructor was not assigned to course")

    def testCourseAssignTa(self):
        self.monkey.get("/edit_section/", {"sectionNumber": "361-401", "teacher": "", "sectionType": "LEC"})
        self.monkey.post("/edit_section/", {"teacher": "miggy@uwm.edu"})
        self.assertEqual(self.cs361.instructor, None, msg="User cannot be assigned to this section")