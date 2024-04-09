from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        (1, 'Parent'),
        (2, 'Student'),
        (3, 'Teacher'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.IntegerField(choices=USER_TYPE_CHOICES)

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    
class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

class Exam(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    date = models.DateField()

class Test(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    date = models.DateField()

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[("Present", "Present"), ("Absent", "Absent")], default="Present")
