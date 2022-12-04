from django.contrib import admin
from django.urls import include, path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('home/', Home.as_view()),
    path('profile/', Profile.as_view()),
    path('new_user/', CreateUser.as_view()),
    path('new_course/', CreateCourse.as_view()),
    path('new_section/', CreateSection.as_view()),
    path('edit_user', EditUser.as_view()),
    path('edit_profile', EditUser.as_view()),
    path('edit_section', EditSection.as_view()),
    path('users/', Users.as_view()),
    path('courses/', Courses.as_view()),
    path('sections/', Sections.as_view()),
    path('notifications/', Notifications.as_view()),
]

