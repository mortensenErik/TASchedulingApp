from django.db import models

# models – essentially, your database layout, with additional metadata.


class UserProfile(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=30)
    officeHours = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    email = models.CharField(max_length=20)


class Course(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    number = models.CharField(max_length=4,unique=True)
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + " " + self.number


class Section(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    number = models.IntegerField
    type = models.CharField(max_length=3)
