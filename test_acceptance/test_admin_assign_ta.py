from django.test import TestCase, Client
from app.models import UserProfile, Course, Section


class testAdminAssignTA(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', role="admin")
        self.frank = UserProfile.objects.create(name='Frank Furter', id='frankf', password='hotdog',
                                                email='frankf@uwm.edu', phone='202-555-0111',
                                                address='abc123', role="TA")
        self.cs361 = Course.objects.create(CourseId='361', name='Intro to Software Engineering', number='361',
                                           subject="COMPSCI")
        self.cs361Lab = Section.objects.create(SectionId='801', type='LAB', course=self.cs361, faculty=None,
                                               number="801")

    def testAssignTA(self):
        self.monkey.get("edit_section", {"sectionNumber": "361-801", "teacher": "", "sectionType": "Lab"})
        self.monkey.post("edit_section", {"teacher": "frankf@uwm.edu"})
        self.assertEqual(self.cs361Lab.faculty, self.frank, msg="TA not assigned to course")
