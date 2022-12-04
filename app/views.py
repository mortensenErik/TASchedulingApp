from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserProfile, Course, Section
from django.contrib.auth import login, logout, authenticate


class Home(HttpResponse):
    def get(self, request):
        return render(request, "Home.html", {})

    def post(self, request):
        logout(request)
        return redirect("Login.html")


class Login(HttpResponse):
    def get(self, request):
        return render(request, "Login.html", {})
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, "Home.html", {})
        else:
            return render(request, "Login.html", {})


class Profile(HttpResponse):
    def get(self, request):
        return render (request, "Profile.html", {})
class createCourse(HttpResponse):
    def get(self, request):
        return render (request, "createCourse.html", {})
class createSection(HttpResponse):
    def get(self, request):
        return render (request, "createSection.html", {})

class createUser(HttpResponse):
    def get(selfself, request):
        return render (request, "createUser.html", {})
class editCourse(HttpResponse):
    def get(self, request):
        return render (request, "editCourse.html", {})

class editProfile(HttpResponse):
    def get(self, request):
        return render (request, "editProfile.html", {})
class editSection(HttpResponse):
    def get(self, request):
        return render (request, "editSection.html", {})
class sendNotifications(HttpResponse):
    def get(self, request):
        return render (request, "sendNotifications.html", {})
class viewCourses(HttpResponse):
    def get(self, request):
        return render (request, "viewCourses.html", {})
class viewSections(HttpResponse):
    def get(self, request):
        return render (request, "viewSections.html", {})
class viewUsers(HttpResponse):
    def get(self, request):
        return render (request, "viewUsers.html", {})