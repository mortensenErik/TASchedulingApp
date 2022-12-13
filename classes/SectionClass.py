from typing import Union
from app.models import Section
from app.models import Course
from app.models import UserProfile


class SectionClass:

    @staticmethod
    def getSectionById(SectionId):
        if id:
            if Section.objects.filter(SectionId=SectionId).exists():
                return Section.objects.get(SectionId=SectionId)
            else:
                return None
        raise TypeError("No parameter provided!")
        
    def getSectionByNumber(number):
        if id:
            if Section.objects.filter(number=number).exists():
                return Section.objects.get(number=number)
            else:
                return None
        raise TypeError("No parameter provided!")

    @staticmethod
    def createSection(SectionId,course, faculty, number, type):
        print('in createSection')
        if SectionClass.getSectionById(SectionId=SectionId) is None:
            if SectionClass.getSectionByNumber(number=number):
                return False
            else:
                Section.objects.create(SectionId=SectionId, course=course, faculty=faculty, number=number, type=type)
                return True
        else:
            return False

    @staticmethod
    def deleteSection(SectionId):
        if id:
            SectionClass.getSectionById(SectionId=SectionId).delete()
        else:
            raise TypeError("No parameter provided!")

    @staticmethod
    def editSection(SectionId,course, faculty, number, type):
        pass
