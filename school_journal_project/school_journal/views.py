from django.shortcuts import render
from .models import Student, Teacher, Grade, Attendance


def student_page(request):
    # Logic to fetch student data, grades, attendance, etc.
    items = Student.objects.all()
    return render(request, 'student_page.html', {"todos": items})


def teacher_page(request):
    # Logic to fetch teacher data, grades, attendance, etc.
    return render(request, 'teacher_page.html', context)


def parent_page(request):
    # Logic to fetch parent data, child grades, attendance, etc.
    return render(request, 'parent_page.html', context)


def home_page(request):
    return render(request, 'home_page.html')
