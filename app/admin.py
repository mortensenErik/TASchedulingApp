from django.contrib import admin
from app.models import UserProfile, Course, Section

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Section)
