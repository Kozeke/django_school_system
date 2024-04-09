# views.py

from django.shortcuts import render
from .models import UserProfile, Grade, Attendance, Parent, Student


def parent_page(request):
    # Assuming parent is authenticated and has access to their children's information
    user_profile = UserProfile.objects.get(user=request.user)
    parent = Parent.objects.get(admin=user_profile)
    children = Student.objects.filter(parent=parent)
    children_grades = {}
    children_attendance = {}

    for child in children:
        grades = Grade.objects.filter(student=child)
        attendance = Attendance.objects.filter(student=child)
        children_grades[child] = grades
        children_attendance[child] = attendance

    context = {
        'children_grades': children_grades,
        'children_attendance': children_attendance,
    }
    return render(request, 'parent_page.html', context)
