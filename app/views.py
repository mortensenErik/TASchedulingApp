from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from classes.UserClass import User
from classes.SectionClass import SectionClass
from classes.CourseClass import CourseClass
from app.models import *
from django.contrib import messages

class Login(View):
    @staticmethod
    def get(request):
        print('in get')
        if 'email' not in request.session:
            print("not in")
            return render(request, "Login.html")
        else:
            print("in")
            return redirect('/home')

    @staticmethod
    def post(request):
        user = User.getUserByEmail(request.POST["email"])
        if user is None or user == '':
            messages.info(request, 'Incorrect username/password. Try again.')
            return render(request, "Login.html", {"error": "User does not exist"})
        else:
            if user.password != request.POST["password"]:
                messages.info(request, 'Incorrect username/password. Try again.')
                return render(request, "login.html", {"error": "Incorrect Password"})
            else:
                request.session["email"] = user.email
                request.session["role"] = user.role
                login(request, user)
                return redirect('home/')




class Home(View):
    @staticmethod
    def get(request):
        return render(request, "Home.html", {"users": UserProfile.objects.all().order_by('name')})

    def post(self, request):
        del request.session["email"]
        del request.session["role"]
        return redirect('/')


class CreateUser(View):
    @staticmethod
    def get(request):
        return render(request, "createUser.html")

    def post(self, request):
        creation = User.createUser(
            # id= request.POST["id"],
            email=request.POST["email"],
            name=request.POST["name"],
            password=request.POST["password"],
            role=request.POST["role"],
            address=request.POST["address"],
            phone=request.POST["phone"]
        )
        if creation:
            print('creation is true')
            return redirect('/users')
        else:
            print('creation is false')
            return render(request, "createUser.html")

class CreateCourse(View):
    @staticmethod
    def get(request):
        return render(request, "createCourse.html")

    @staticmethod
    def post(request):
        creation = CourseClass.createCourse(
            # CourseId=request.POST["CourseId"],
            name=request.POST["name"],
            subject=request.POST["subject"],
            number=int(request.POST["number"])
        )
        if creation:
            print('creation is true')
            return redirect('/courses')
        else:
            print('creation is false')
            return render(request, "createCourse.html")



class CreateSection(View):
    @staticmethod
    def get(request):
        return render(request, "createSection.html", {'courses': Course.objects.all(), 'users': UserProfile.objects.all()})

    @staticmethod
    def post(request):
        course = CourseClass.getCourseById(CourseId=request.POST["course"])
        faculty = None
        if request.POST["faculty"]:
            faculty = User.getUserByEmail(request.POST["faculty"])
            print('FACULTY')
            print(faculty)
        creation = SectionClass.createSection(
            course=course,
            faculty=faculty,
            number=int(request.POST["number"]),
            type=request.POST["type"],
        )
        if creation:
            print('creation is true')
            return redirect('/sections')
        else:
            print('creation is false')
            return render(request, "createCourse.html")


class Profile(View):
    @staticmethod
    def get(request):
        print("It came back here")
        return render(request, "Profile.html",
                      {"user": User.getUserByEmail(request.session["email"])})

    @staticmethod
    def post(request, editing):
        print("editing: ", editing)
        request.session["editing"] = editing
        return render(request, "Profile.html",
                      {"user": User.getUserByEmail(request.session["email"])})


class EditProfile(View):

    @staticmethod
    def get(request):
        return render(request, "editProfile.html", {"user": User.getUserByEmail(request.session["email"])})

    @staticmethod
    def post(request):
        User.editProfileInfo(
            name=request.POST['name'],
            email=request.POST['email'],
            address=request.POST['address'],
            phone=request.POST['phone'],
        )
        return redirect('/profile/')


class Users(View):
    @staticmethod
    def get(request):
        return render(request, "viewUsers.html", {"users": UserProfile.objects.all().order_by
                                                    ('role', 'name').values()})

    @staticmethod
    def post(request, email):
        User.deleteUser(email)
        return redirect('/users')

class Sections(View):
    @staticmethod
    def get(request):
        return render(request, "viewSections.html", {"sections": Section.objects.all().order_by(
                                'course__subject', 'course__number', 'number')})

    @staticmethod
    def post(request, SectionId):
        SectionClass.deleteSection(SectionId)
        return redirect('/sections')

class Courses(View):
    @staticmethod
    def get(request):
        return render(request, "viewCourses.html", {"courses": Course.objects.all().order_by(
                                                                        'subject', 'number')})

    @staticmethod
    def post(request, CourseId):
        CourseClass.deleteCourse(CourseId)
        return redirect('/courses')

class EditUser(View):
    @staticmethod
    def get(request, id):
        user_to_edit = UserProfile.objects.get(id=id)
        return render(request, "editUser.html",  {"user": user_to_edit})

    @staticmethod
    def post(request, id):
        user = UserProfile.objects.get(id=id)
        user.email = request.POST['email']
        user.name = request.POST['name']
        role = request.POST.get('role', False)
        if role:
            user.role = role
        user.address = request.POST['address']
        user.phone = request.POST['phone']
        user.save()
        return redirect('/users/')


class EditCourse(View):
    @staticmethod
    def get(request, id):
        course_to_edit = Course.objects.get(CourseId=id)
        return render(request, "editCourse.html", {'course': course_to_edit})

    @staticmethod
    def post(request, id):
        course = Course.objects.get(CourseId=id)
        course.name = request.POST['name']
        course.number = request.POST['number']
        course.subject = request.POST['subject']
        course.save()
        return redirect('/courses/')


class EditSection(View):
    @staticmethod
    def get(request, id):
        current_section = SectionClass.getSectionById(id)
        return render(request, "editSection.html",
                      {"section": current_section, 'courses': Course.objects.all(), 'users': UserProfile.objects.all()})

    @staticmethod
    def post(request, id):
        section = Section.objects.get(SectionId=id)
        courseId = request.POST.get('course', False)
        facultyId = request.POST.get('faculty', False)
        type = request.POST.get('type', False)
        number = request.POST['number']
        section.number = number
        if facultyId:
            faculty = UserProfile.objects.get(id=facultyId)
            section.faculty = faculty
        if courseId:
            course = Course.objects.get(CourseId=courseId)
            section.course = course
        if type:
            section.type = type
        section.save()
        return redirect('/sections/')


class Notifications(View):
    @staticmethod
    def get(request):
        return render(request, "sendNotifications.html")

class confirmDeleteUser(View):
    @staticmethod
    def get(request, userID):
        return render(request, "confirmDeleteUser.html", {"user": UserProfile.objects.filter(id=userID).first()})

class confirmDeleteCourse(View):
    @staticmethod
    def get(request, courseID):
        return render(request, "confirmDeleteCourse.html", {"course": Course.objects.filter(CourseId=courseID).first()})

class confirmDeleteSection(View):
    @staticmethod
    def get(request, sectionID):
            return render(request, "confirmDeleteSection.html", {"section": Section.objects.filter(SectionId=sectionID).first()})

class assignTA(View):
    pass
