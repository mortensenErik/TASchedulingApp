from typing import Union
from app.models import Section
from app.models import Course
from app.models import UserProfile


class SectionClass:
    # def __init__(self, message):
    #     self.__message = message
    #
    # def __str__(self):
    #     return self.__message
    #
    # def __bool__(self):
    #     return False
    #
    # def verify_dict(needed: list[(str, type)], toVerify: dict) -> Union[ErrorString, bool]:
    #     for i in needed:
    #         if not toVerify.get(i[0]):
    #             return ErrorString("Error: " + i[0] + " was not provided")
    #         if type(toVerify[i[0]]) is not i[1]:
    #             return ErrorString("Error: invalid datatype for " + i[0])
    #
    #     return True

    @staticmethod
    def getSectionById(SectionId):
        if id:
            if Section.objects.filter(SectionId=SectionId).exists():
                return Section.objects.get(SectionId=SectionId)
            else:
                return None
        raise TypeError("No parameter provided!")

    @staticmethod
    def createSection(SectionId,course, faculty, number, type):
        print('in createSection')
        if SectionClass.getSectionById(SectionId=SectionId) is None:
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