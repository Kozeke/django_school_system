from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed


class Subject(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField()
    date = models.DateField()
    # Add more fields as needed


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)
    # Add more fields as needed
