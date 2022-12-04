from django.contrib import admin
from django.urls import include, path
from app.views import *

urlpatterns = [
    path('', Login.as_view()),
    path('admin/', admin.site.urls),
]