from typing import Union
from app.models import Section
from app.models import Course
from app.models import UserProfile

class ErrorString:
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message

    def __bool__(self):
        return False

def verify_dict(needed: list[(str, type)], toVerify: dict) -> Union[ErrorString, bool]:
    for i in needed:
        if not toVerify.get(i[0]):
            return ErrorString("Error: " + i[0] + " was not provided")
        if type(toVerify[i[0]]) is not i[1]:
            return ErrorString("Error: invalid datatype for " + i[0])

    return True

def make_section(secinfo: dict) -> Union[ErrorString, bool]:
        """handles making a section given the user sections data. On failure, return ErrorString
        describing error. On success, return True"""
        #here id in needed is the id of the Course, not the scetion
        needed = [("id",str ), ("section", int), ("number", int),("type", str)]
        check = verify_dict(needed, secinfo)
        if not check:
            return check

        if Section.objects.filter(section__id__exact=secinfo["number"]).exists():
            return ErrorString("Error: this number section for this course already exists")

        lookfor = Course.objects.filter(number__exact=secinfo["id"])
        if not lookfor.exists():
            return ErrorString("Error: course does not exist")

        Section.objects.create(course=(list(lookfor))[0], number=secinfo["number"],type=secinfo["type"] )
        return True
