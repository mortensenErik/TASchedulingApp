from django.test import TestCase
#
from app.models import Section
from app.models import Course
from classes import SectionClass
from classes.SectionClass import make_section
#
#
# class TestSection(TestCase):
#
#     def setUp(self):
#         self.cs361 = Section.objects.create(name='CompSci 361', number=101, ta='ravipati_ta',
#                                             type='lab')
#         self.cs371 = Section.objects.create(name='CompSci 371', number=1234, ta='ravipati_In',
#                                             type='sec')
#         self.cs381 = Section.objects.create(name='CompSci 381', number=1263, ta='pavipati_ta',
#                                             type='lab')
#         self.cs391 = Section.objects.create(name='CompSci 391', number=1223, ta='jvipati_In',
#                                             type='sec')
#         self.cs401 = Section.objects.create(name='CompSci 401', number=1523, ta='kaipati_In',
#                                             type='sec')
#         self.cs411 = Section.objects.create(name='CompSci 411', number=1293, ta='saipati_ta',
#                                             type='lab')
#         self.cs421 = Section.objects.create(name='CompSci 421', number=1273, ta='jipati_In',
#                                             type='sec')
#
#     def test_section_delete(self):
#         self.cs361.delete()
#         self.assertEqual(len(list(Section.objects), 6))
#
#     def test_section_Number_Edit(self):
#         self.cs371.number = 321
#         self.assertEqual(self.cs371.number, 321)
#
#     def test_edit_Ta(self):
#         self.cs381.ta = 'non-pavipati_ta'
#         self.assertEqual(self.cs381.ta, 'non-pavipati_ta')
#
#
#     def test_edit_Teacher(self):
#         self.cs391.ta = 'jaavipati_In'
#         section = SectionClass()
#         self.assertEqual(self.cs391.ta, 'jaavipati_In')
#         self.assertEqual(section.set_teacher(),
#                          )
#         teach_lookup = list(Section.objects.filter(ta='jvipati_In'))
#         self.assertEqual(len(teach_lookup), 0)
#
#     # may need to change from 7 to 6 if needed... not sure if editing the stuff in first test will edit the db or not
#     def test_delete_lookup(self):
#         self.cs411.delete()
#         self.assertEqual(len(list(Section.objects), 7))
#         section_lookup = list(Section.objects.filter(name='CompSci 411'))
#         self.assertEqual(len(section_lookup), 0)
#
#     def test_sec_type_edit(self):
#         self.cs401.type = 'lab'
#         self.assertEqual(self.cs401.type, 'lab')

#still working on it not done
class CreateSectionTest(TestCase):
    def setUp(self):
        self.tempCourse = Course(name="compsci", number="351",
                                 id="1253", instructor="human")
        self.tempCourse.save()

    def test_section_things(self):
        okay = make_section({"id": "idnumber"})