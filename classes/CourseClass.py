from typing import Union
from app.models import Course


class CourseClass:

    @staticmethod
    def getCourseById(CourseId):
        if CourseId:
            if Course.objects.filter(CourseId=CourseId).exists():
                return Course.objects.get(CourseId=CourseId)
            else:
                return None
        raise ValueError("No parameter provided!")

    @staticmethod
    def createCourse(name, subject, number):
        if not name or not subject or not number:
            raise ValueError("You passed in a null parameter!")
        if len(number) > 3:
            raise ValueError("Number is too big!")
        if Course.objects.filter(name=name):
            raise ValueError("Duplicate name!")
        Course.objects.create(name=name, subject=subject, number=number)
        return True

    @staticmethod
    def deleteCourse(CourseId):
        if CourseId:
            course = CourseClass.getCourseById(CourseId=CourseId)
            if course:
                course.delete()
            else:
                raise ValueError("this course does not exist!")
        else:
            raise ValueError("No parameter provided!")

