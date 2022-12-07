from typing import Union
from app.models import Course


class CourseClass:

    @staticmethod
    def getCourseById(id):
        if id:
            if Course.objects.filter(id=id).exists():
                return Course.objects.get(id=id)
            else:
                return None
        raise TypeError("No parameter provided!")

# class ErrorString:
#
#     def __init__(self, id, name, instructor, number, sections):
#         def __init__(self, message):
#             self.message = message
#
#         def __str__(self):
#             return self.message
#
#         def __bool__(self):
#             return False

#
# def verify_dict(needed: list[(str, type)], toVerify: dict) -> Union[ErrorString, bool]:
#     for i in needed:
#         if not toVerify.get(i[0]):
#             return ErrorString("Error: " + i[0] + " was not provided")
#         if type(toVerify[i[0]]) is not i[1]:
#             return ErrorString("Error: invalid type for " + i[0])
#
#     return True
#
#
# def make_course(courseinfo: dict) -> Union[ErrorString, bool]:
#     """
#     makes a course. returns an ErrorString, describing the error, if fails to create a course.
#     returns true if successfully created a new course
#     """
#     needed = [("id", str), ("name", str), ("number", int), ("instructor", str)]
#     check = verify_dict(needed, courseinfo)
#
#     if not check:
#         return check
#
#     lookup = Course.objects.filter(number = courseinfo["number"]).exists()
#
#     if lookup:
#         return ErrorString("Error: this course already exists, enter another course number to add")
#     else:
#         Course.objects.create(name = courseinfo["name"], number = courseinfo["number"])
#
#     return True
#
#
# def delete_course(courseinfo: dict) -> Union[ErrorString, bool]:
#     """
#     deletes a course, returns an ErrorString if fails to delete course. return true if successfully
#     deletes a course
#     """
#     needed = [("id", str), ("name", str), ("number", int), ("instructor", str)]
#     check = verify_dict(needed, courseinfo)
#
#     if not check:
#         return check
#
#     lookup = Course.objects.filter(number = courseinfo["number"]).exists()
#
#     if lookup:
#         Course.objects.delete(name = courseinfo["name"], number = courseinfo["number"])
#     else:
#         return ErrorString("Error: this course has not been created, unable to delete")
#
#     return True
#
#
#     def assign_instructor_to_course(courseinfo: dict) -> Union[ErrorString, bool]:
#         """
#         assigns an instructor to a course. if an instructor is already assigned, the new instructor
#         will be added replacing old instructor
#         """
#         needed = [("id", str), ("name", str), ("number", int), ("instructor", str)]
#         check = verify_dict(needed, courseinfo)
#
#         if not check:
#             return check
#
#         lookup = Course.objects.filter(number = courseinfo["number"]).exists()
#
#         if lookup:
#             Course.objects.update(name = courseinfo["name"], number = courseinfo["number"], instructor = courseinfo["instructor"])
#         else:
#             return ErrorString("Error: course has not been created, unable to assign instructor")
#
#         return True

