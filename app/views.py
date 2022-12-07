from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from classes.UserClass import User


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
        return render(request, "Home.html")

    def post(self, request):
        del request.session["email"]
        del request.session["role"]
        return redirect('/')


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
        return render(request, "Profile.html",
                      {"user": User.getUserByEmail(request.session["email"])})


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