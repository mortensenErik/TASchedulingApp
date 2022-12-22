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
        raise TypeError("No parameter provided!")

    @staticmethod
    def createCourse(name, subject, number):
        Course.objects.create(name=name, subject=subject, number=number)
        return True

    @staticmethod
    def deleteCourse(CourseId):
        if id:
            CourseClass.getCourseById(CourseId=CourseId).delete()
        else:
            raise TypeError("No parameter provided!")

