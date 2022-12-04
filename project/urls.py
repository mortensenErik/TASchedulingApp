from django.contrib import admin
from django.urls import include, path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('home/', Home.as_view()),
    path('new_user/', CreateUser.as_view()),
    path('new_course/', CreateCourse.as_view()),
    path('new_section/', CreateSection.as_view()),
]