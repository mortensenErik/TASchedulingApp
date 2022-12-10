from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from classes.UserClass import User
from classes.SectionClass import SectionClass
from classes.CourseClass import CourseClass
from app.models import *


class Login(View):
    @staticmethod
    def get(request):
        print('in get')
        if 'email' not in request.session:
            print("not in")
            return render(request, "Login.html")
        else:
            print("in")
            return redirect('/home')

    @staticmethod
    def post(request):
        user = User.getUserByEmail(request.POST["email"])
        if user is None:
            return render(request, "Login.html", {"error": "User does not exist"})
        else:
            if user.password != request.POST["password"]:
                return render(request, "login.html", {"error": "Incorrect Password"})
            else:
                request.session["email"] = user.email
                request.session["role"] = user.role
                return redirect('home/')




class Home(View):
    @staticmethod
    def get(request):
        return render(request, "Home.html", {"users": UserProfile.objects.all()})

    def post(self, request):
        del request.session["email"]
        del request.session["role"]
        return redirect('/')


class CreateUser(View):
    @staticmethod
    def get(request):
        return render(request, "createUser.html")

    def post(self, request):
        creation = User.createUser(
            id= request.POST["id"],
            email=request.POST["email"],
            name=request.POST["name"],
            password=request.POST["password"],
            role=request.POST["role"],
            address=request.POST["address"],
            phone=request.POST["phone"]
        )
        if creation:
            print('creation is true')
            return redirect('/users')
        else:
            print('creation is false')
            return render(request, "createUser.html")

class CreateCourse(View):
    @staticmethod
    def get(request):
        return render(request, "createCourse.html")

    @staticmethod
    def post(request):
        creation = CourseClass.createCourse(
            CourseId=request.POST["CourseId"],
            name=request.POST["name"],
            subject=request.POST["subject"],
            number=int(request.POST["number"])
        )
        if creation:
            print('creation is true')
            return redirect('/courses')
        else:
            print('creation is false')
            return render(request, "createCourse.html")



class CreateSection(View):
    @staticmethod
    def get(request):
        return render(request, "createSection.html", {'courses': Course.objects.all(), 'users': UserProfile.objects.all()})

    @staticmethod
    def post(request):
        course = CourseClass.getCourseById(CourseId=request.POST["course"])
        faculty = None
        if request.POST["faculty"]:
            faculty = User.getUserByEmail(request.POST["faculty"])
        creation = SectionClass.createSection(
            SectionId=request.POST["SectionId"],
            course=course,
            faculty=faculty,
            number=int(request.POST["number"]),
            type=request.POST["type"],
        )
        if creation:
            print('creation is true')
            return redirect('/sections')
        else:
            print('creation is false')
            return render(request, "createCourse.html")


class Profile(View):
    @staticmethod
    def get(request):
        print("It came back here")
        return render(request, "Profile.html",
                      {"user": User.getUserByEmail(request.session["email"])})

    @staticmethod
    def post(request, editing):
        print("editing: ", editing)
        request.session["editing"] = editing
        return render(request, "Profile.html",
                      {"user": User.getUserByEmail(request.session["email"])})


class Users(View):
    @staticmethod
    def get(request):
        return render(request, "viewUsers.html", {"users": UserProfile.objects.all()})

    @staticmethod
    def post(request, email):
        User.deleteUser(email)
        return redirect('/users')

class Sections(View):
    @staticmethod
    def get(request):
        return render(request, "viewSections.html", {"sections": Section.objects.all()})

    @staticmethod
    def post(request, SectionId):
        SectionClass.deleteSection(SectionId)
        return redirect('/sections')

class Courses(View):
    @staticmethod
    def get(request):
        return render(request, "viewCourses.html", {"courses": Course.objects.all()})

    @staticmethod
    def post(request, CourseId):
        CourseClass.deleteCourse(CourseId)
        return redirect('/courses')

class EditUser(View):
    @staticmethod
    def get(request, email):
        user_to_edit = User.getUserByEmail(email)
        return render(request, "editUser.html",  {"user": user_to_edit})

    @staticmethod
    def post(request):
        User.editUser(
            id=request.POST["id"],
            email=request.POST["email"],
            name=request.POST["name"],
            password=request.POST["password"],
            role=request.POST.get('role', False),
            address=request.POST["address"],
            phone=request.POST["phone"]
        )
        return redirect('/users/')


class EditCourse(View):
    @staticmethod
    def get(request, CourseId):
        course_to_edit = CourseClass.getCourseById(CourseId)
        return render(request, "editCourse.html", {'course': course_to_edit})

    @staticmethod
    def post(request):
        CourseClass.editCourse(
            CourseId=request.POST['CourseId'],
            name=request.POST['name'],
            subject=request.POST['subject'],
            number=request.POST['number'],
        )
        return redirect('/courses/')



class EditSection(View):
    @staticmethod
    def get(request, SectionId):
        current_section = SectionClass.getSectionById(SectionId)
        return render(request, "editSection.html",
                      {"section": current_section, 'courses': Course.objects.all(), 'users': UserProfile.objects.all()})

    @staticmethod
    def post(request):
        faculty = False
        if request.POST.get('faculty', False):
            faculty = User.getUserByEmail('faculty')
        SectionClass.editSection(
            SectionId=request.POST['SectionId'],
            course=request.POST.get('course', False),
            number=request.POST['number'],
            faculty=request.POST.get('faculty', False),
            type=request.POST.get('type', False)
        )
        return redirect('/sections/')


class Notifications(View):
    @staticmethod
    def get(request):
        return render(request, "sendNotifications.html")