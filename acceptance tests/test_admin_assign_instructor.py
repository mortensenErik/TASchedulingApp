from django.test import TestCase, Client
from app.models import UserProfile, Course, Section


class testAdminAssignInstructor(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', officeHours="Appointment Only",
                                                role="Instructor")
        self.Miguel = UserProfile.objects.create(name='Miguel', id='miggy', password='ziggy', email='miggy@uwm.edu',
                                                phone='202-555-0190', address='abc120', officeHours="Always",
                                                role="TA")
        self.cs361 = Course.objects.create(id='361', name='Intro to Software Engineering', number='CS361',
                                           instructor=None)
    def testAssignInstructor(self):
        self.monkey.get("edit_course/", {"courseName": "Intro to Software Engineering", "courseNumber": "CS361"})
        self.monkey.post("edit_course/", {"courseInstructor": "bigboy@uwm.edu"})
        self.assertEqual(self.cs361.instructor, self.nigel, msg="Instructor not assigned to course")

    def testCourseAssignTa(self):
        self.monkey.get("edit_course/", {"courseName": "Intro to Software Engineering", "courseNumber": "CS361"})
        self.monkey.post("edit_course/", {"courseInstructor": "miggy@uwm.edu"})
        self.assertEqual(self.cs361.instructor, None, msg="User cannot be assigned to course")