from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from classes.UserClass import User

class Login(View):
    @staticmethod
    def get(request):
        # request.session["username"] = None
        # request.session["current"] = ""
        # request.session["user_type"] = None
        # request.session["user_id"] = None
        return render(request, "Login.html")

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        # if form.is_valid():
        #     user = form.get_user()
        #     login(request, user)
        if User.doesUserExist(request.POST["username"]):
            print("Condition succeeded")
            return render(request, "Home.html", {})
        else:
            return render(request, "Login.html", {})


class Home(View):
    @staticmethod
    def get(request):
        return render(request, "Home.html")

    def post(self, request):
        logout(request)
        return redirect("Login.html")


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