from django.contrib import admin
from django.urls import include, path
from app.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('home/', Home.as_view()),
    path('profile/', Profile.as_view()),
    path('profile/<int:editing>', Profile.as_view()),
    path('edit_profile/', EditProfile.as_view()),
    path('new_user/', CreateUser.as_view()),
    path('new_course/', CreateCourse.as_view()),
    path('new_section/', CreateSection.as_view()),
    path('edit_user', EditUser.as_view()),
    path('edit_user/<str:id>/', EditUser.as_view()),
    path('edit_course', EditCourse.as_view()),
    path('edit_course/<str:id>/', EditCourse.as_view()),
    path('edit_section', EditSection.as_view()),
    path('edit_section/<str:id>/', EditSection.as_view()),
    path('users/', Users.as_view()),
    path('users/<str:email>/', Users.as_view()),
    path('courses/', Courses.as_view()),
    path('courses/<str:CourseId>/', Courses.as_view()),
    path('sections/', Sections.as_view()),
    path('sections/<str:SectionId>/', Sections.as_view()),
    path('notifications/', Notifications.as_view()),
    path('confirmDeleteUser/<str:userID>/', confirmDeleteUser.as_view(), name="confirmDeleteUser"),
    path('confirmDeleteCourse/<str:courseID>/', confirmDeleteCourse.as_view(), name="confirmDeleteCourse"),
    path('confirmDeleteSection/<str:sectionID>/', confirmDeleteSection.as_view(), name="confirmDeleteSection"),
    path('assignTa/<str:id>/', assignTA.as_view())
]

urlpatterns += staticfiles_urlpatterns()

