from django.db import models

# models – essentially, your database layout, with additional metadata.


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=[('ADMIN', 'admin'), ('INSTRUCTOR', 'Instructor'), ('TA', 'TA')])
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.role + ": " + self.name

    def get_model_fields(model):
        return model._meta.fields


class Course(models.Model):
    CourseId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    number = models.CharField(max_length=3)
    subject = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.subject + " " + self.number.__str__() + ": " + self.name


class Section(models.Model):
    SectionId = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(UserProfile, on_delete= models.SET_NULL, null=True, blank=True)
    number = models.CharField(max_length=3)
    type = models.CharField(max_length=3, choices=[('LEC', 'lecture'), ('LAB', 'lab')])

    def __str__(self):
        return self.type + ": " + self.course.number.__str__() + "-" + self.number.__str__()

