from django.test import TestCase

from classes.CourseClass import *


class TestCourse(TestCase):

    def setUp(self):
        self.CS361 = Course.objects.create(name="Introduction to Software Engineering", number="361",
                                           subject="CS")
        self.CS250 = Course.objects.create(name="Introductory Computer Programming", number="250", subject="CS")
        self.CS251 = Course.objects.create(name="Intermediate Computer Programming", number="251", subject="CS")

    def test_get_course(self):
        course = CourseClass.getCourseById(self.CS250.CourseId)
        self.assertEqual(course.CourseId, self.CS250.CourseId)
        self.assertEqual(course.name, self.CS250.name)
        self.assertEqual(course.subject, self.CS250.subject)
        self.assertEqual(course.number, self.CS250.number)

    def test_get_course_bad(self):
        with self.assertRaises(ValueError, msg="Null parameter") as context:
            CourseClass.getCourseById(None)

    def test_get_course_not_doesnt_exist(self):
        course = CourseClass.getCourseById(2810271937129131)
        self.assertEqual(course, None)

    def test_course_made(self):
        test = CourseClass.createCourse(name="Data Structures and Algorithms", number="351", subject="CS")
        lookup = list(Course.objects.all())
        self.assertEqual(len(lookup), 4, msg="Error: course was not created")

    def test_create_null_name(self):
        with self.assertRaises(ValueError, msg="Null name!") as context:
            CourseClass.createCourse(name=None, number="351", subject="CS")

    def test_create_null_number(self):
        with self.assertRaises(ValueError, msg="Null number!") as context:
            CourseClass.createCourse(name="Data Structures and Algorithms", number=None, subject="CS")

    def test_create_null_subject(self):
        with self.assertRaises(ValueError, msg="Null number!") as context:
            CourseClass.createCourse(name="Data Structures and Algorithms", number="351", subject=None)

    def test_create_bad_number(self):
        with self.assertRaises(ValueError, msg="Bad number!") as context:
            CourseClass.createCourse(name="Data Structures and Algorithms", number="3533", subject="COMPSCI")

    def test_create_dup_course(self):
        with self.assertRaises(ValueError, msg="course with this name already exists") as context:
            CourseClass.createCourse(name="Introduction to Software Engineering", number="361", subject="CS")

    def test_delete_null(self):
        with self.assertRaises(ValueError, msg="Paremeter is null") as context:
            CourseClass.deleteCourse(None)

    def test_delete_nonexistent_course(self):
        with self.assertRaises(ValueError, msg="This course does not exist") as context:
            CourseClass.deleteCourse(3244242342)

    def test_delete_all_course(self):
        for course in Course.objects.all():
            CourseClass.deleteCourse(course.CourseId)
        size = len(Course.objects.all())
        self.assertEqual(size, 0, msg="Failed to delete all courses")
