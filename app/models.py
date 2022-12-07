from django.db import models

# models – essentially, your database layout, with additional metadata.


class UserProfile(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=[('ADMIN', 'admin'), ('INSTRUCTOR', 'Instructor'), ('TA', 'TA')])
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.role + ": " + self.name


class Course(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    number = models.CharField(max_length=4,unique=True)

    def __str__(self):
        return self.name + " " + self.number


class Section(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    number = models.IntegerField(default=0)
    type = models.CharField(max_length=3, choices=[('LEC', 'lecture'), ('LAB', 'lab')])

    def __str__(self):
        return self.course.number + "-" + self.number.__str__()

