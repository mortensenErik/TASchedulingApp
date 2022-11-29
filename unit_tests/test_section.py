from django.test import TestCase

from app.models import Section


class TestSection(TestCase):

    def setUp(self):
        self.cs361 = Section.objects.create(course_name='CompSci 361', Hyphen_after_No=101, Taught_By_Ta='ravipati_ta',
                                            SectionType='lab')
        self.cs371 = Section.objects.create(course_name='CompSci 371', Hyphen_after_No=1234, Taught_By_In='ravipati_In',
                                            SectionType='sec')
        self.cs381 = Section.objects.create(course_name='CompSci 381', Hyphen_after_No=1263, Taught_By_Ta='pavipati_ta',
                                            SectionType='lab')
        self.cs391 = Section.objects.create(course_name='CompSci 391', Hyphen_after_No=1223, Taught_By_In='jvipati_In',
                                            SectionType='sec')
        self.cs401 = Section.objects.create(course_name='CompSci 401', Hyphen_after_No=1523, Taught_By_In='kaipati_In',
                                            SectionType='sec')
        self.cs411 = Section.objects.create(course_name='CompSci 411', Hyphen_after_No=1293, Taught_By_Ta='saipati_ta',
                                            SectionType='lab')
        self.cs421 = Section.objects.create(course_name='CompSci 421', Hyphen_after_No=1273, Taught_By_In='jipati_In',
                                            SectionType='sec')

    def test_section_delete(self):
        self.cs361.delete()
        self.assertEqual(len(list(Section.objects), 6))

    def test_section_Number_Edit(self):
        self.cs371.Hyphen_after_No = 321
        self.assertEqual(self.cs371.Hyphen_after_No, 321)

    def test_edit_Ta(self):
        self.cs381.Taught_By_Ta = 'non-pavipati_ta'
        self.assertEqual(self.cs381.Taught_By_Ta, 'non-pavipati_ta')

    def test_edit_Teacher(self):
        self.cs391.Taught_By_In = 'jaavipati_In'
        self.assertEqual(self.cs391.Taught_By_In, 'jaavipati_In')
        teach_lookup = list(Section.objects.filter(Taught_By_In='jvipati_In'))
        self.assertEqual(len(teach_lookup), 0)

    # may need to change from 7 to 6 if needed... not sure if editing the stuff in first test will edit the db or not
    def test_delete_lookup(self):
        self.cs411.delete()
        self.assertEqual(len(list(Section.objects), 7))
        section_lookup = list(Section.objects.filter(course_name='CompSci 411'))
        self.assertEqual(len(section_lookup), 0)

    def test_sec_type_edit(self):
        self.cs401.SectionType = 'lab'
        self.assertEqual(self.cs401.SectionType, 'lab')
