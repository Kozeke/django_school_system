from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(models.Model):
    PARENT = 1
    STUDENT = 2
    TEACHER = 3

    USER_TYPE_CHOICES = (
        (PARENT, 'Parent'),
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.IntegerField(choices=USER_TYPE_CHOICES)
    objects = models.Manager()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    admin = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    objects = models.Manager()


class Parent(models.Model):
    name = models.CharField(max_length=100)
    admin = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    objects = models.Manager()


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    objects = models.Manager()


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    admin = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson, related_name="students", null=True)
    objects = models.Manager()


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2,
                                validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    objects = models.Manager()


class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    objects = models.Manager()


class Test(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    date = models.DateField()


class Attendance(models.Model):
    PRESENT = "Present"
    ABSENT = "Absent"

    STATUS_CHOICES = (
        (PRESENT, 'Present'),
        (ABSENT, 'Absent'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PRESENT)
    objects = models.Manager()
