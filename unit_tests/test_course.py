from django.test import TestCase

from app.models import Course


class TestCourse(TestCase):

    def setUp(self):
        self.courseWord = Course.objects.create(course_name='CompSci', Hyphen_before_No='250', instructor='Rama_In')
        self.courseWord2 = Course.objects.create(course_name='CompSci', Hyphen_before_No='251',
                                                 instructor='Rama_In')
        self.courseWord3 = Course.objects.create(course_name='CompSci', Hyphen_before_No='251',
                                                 instructor='sama_In')
        self.courseWord4 = Course.objects.create(course_name='CompSci', Hyphen_before_No='351',
                                                 instructor='jama_In')

    def test_course(self):
        course_lookup = list(Course.objects.filter(course_name='CompSci'))
        course_lookup2 = list(Course.objects.filter(Hyphen_before_No='251'))
        self.assertEqual(course_lookup, 0)
        self.assertFalse(list(Course.objects.filter(course_name='CompSci').exists(),
                              msg="Error: course data is not stored when created... Failed"))
        self.assertEqual(course_lookup2, 0)
        self.assertFalse(course_lookup2.exists(), msg="Error: course data is not stored when created... Failed")

    def test_instructor(self):
        self.courseWord4.instructor = 'Rama_In'
        self.assertEqual(self.courseWord4.instructor, 'Rama_In')
