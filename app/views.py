from django.http import HttpResponse
from django.shortcuts import render

class Home(HttpResponse):
    def get(self, request):
        return render (request, "Home.html", {})
class Login(HttpResponse):
    def get(self, request):
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
class editCourse(HttpResponse):
    def get(self, request):
        return render (request, "editCourse.html", {})
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