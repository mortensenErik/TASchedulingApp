from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect


class Login(View):
    @staticmethod
    def get(request):
        # request.session["username"] = None
        # request.session["user_type"] = None
        # request.session["user_id"] = None
        return render(request, "Login.html")
