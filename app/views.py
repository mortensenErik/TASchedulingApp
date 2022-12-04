from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect


class Login(View):
    @staticmethod
    def get(request):
        # request.session["username"] = None
        # request.session["current"] = ""
        # request.session["user_type"] = None
        # request.session["user_id"] = None
        return render(request, "Login.html")


class Home(View):
    @staticmethod
    def get(request):
        return render(request, "Home.html")


class CreateUser(View):
    @staticmethod
    def get(request):
        return render(request, "createUser.html")


class CreateCourse(View):
    @staticmethod
    def get(request):
        return render(request, "createCourse.html")


class CreateSection(View):
    @staticmethod
    def get(request):
        return render(request, "createSection.html")


class Profile(View):
    @staticmethod
    def get(request):
        return render(request, "Profile.html")


class Users(View):
    @staticmethod
    def get(request):
        return render(request, "viewUsers.html")


class Sections(View):
    @staticmethod
    def get(request):
        return render(request, "viewSections.html")


class Courses(View):
    @staticmethod
    def get(request):
        return render(request, "viewCourses.html")


class EditUser(View):
    @staticmethod
    def get(request):
        return render(request, "editProfile.html")


class EditCourse(View):
    @staticmethod
    def get(request):
        return render(request, "editCourse.html")


class EditSection(View):
    @staticmethod
    def get(request):
        return render(request, "editSection.html")


class Notifications(View):
    @staticmethod
    def get(request):
        return render(request, "sendNotifications.html")