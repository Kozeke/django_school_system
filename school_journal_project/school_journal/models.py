from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now


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
    admin = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True)
    lessons = models.ManyToManyField(
        Lesson, related_name="students", null=True)
    objects = models.Manager()


class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    date_time = models.DateTimeField(default=now)
    objects = models.Manager()


class Test(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    date_time = models.DateTimeField(default=now)


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, null=True, blank=True)
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, null=True, blank=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2,
                                validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    def clean(self):
        # Ensure either exam or test is set, not both or none
        if self.exam is None and self.test is None:
            raise ValidationError(
                "Either an exam or a test must be provided for the grade.")
        if self.exam is not None and self.test is not None:
            raise ValidationError(
                "Please provide either an exam or a test, not both.")

    objects = models.Manager()


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
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=PRESENT)
    objects = models.Manager()
