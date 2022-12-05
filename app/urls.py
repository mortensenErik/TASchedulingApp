from django.urls import path
from app.views import *
from . import views


urlpatterns = [
    path('', Login.as_view()),
    path('createCourse/', createCourse.as_view()),
    path('createSection/', createSection.as_view()),
    path('createUser/', createUser.as_view()),
    path('editCourse/', editCourse.as_view()),
    path('editProfile/', editProfile.as_view()),
    path('editSection/', editSection.as_view()),
    path('Home/', Home.as_view()),
    path('Profile/', Profile.as_view()),
    path('sendNotifications/', sendNotifications.as_view()),
    path('viewCourses/', viewCourses.as_view()),
    path('viewSections/', viewSections.as_view()),
    path('viewUsers/', viewUsers.as_view())
]