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

