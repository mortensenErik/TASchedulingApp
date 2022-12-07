from django.test import TestCase, Client
from app.models import UserProfile, Course, Section


class testAdminAssignTA(TestCase):
    def setUp(self):
        self.monkey = Client()
        self.nigel = UserProfile.objects.create(name='Nigel', id='bigboy', password='boogy', email='bigboy@uwm.edu',
                                                phone='202-555-0196', address='abc123', officeHours="Appointment Only",
                                                role="admin")
        self.frank = UserProfile.objects.create(name='Frank Furter', id='frankf', password='hotdog',
                                                email='frankf@uwm.edu',
                                                phone='202-555-0111', address='abc123', officeHours="Appointment Only",
                                                role="TA")
        self.cs361 = Course.objects.create(id='361', name='Intro to Software Engineering', number='CS361',
                                           instructor=None)
        self.cs361Lab = Section.objects.create(id='801', type='Lab', course=self.cs361, teacher=None)

    def testAssignTA(self):
        self.monkey.get("/editSection/", {"sectionNumber": "361-801", "sectionLeader": "", "sectionType": "Lab"})
        self.monkey.post("/editSection/", {"teacher": "frankf@uwm.edu"})
        self.assertEqual(self.cs361Lab.teacher, self.frank, msg="TA not assigned to course")
