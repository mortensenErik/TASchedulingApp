from django.urls import path
from app.views import *
from . import views

urlpatterns = [
    path('', Login.as_view()),
]