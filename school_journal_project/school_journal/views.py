from django.shortcuts import render
from .models import Lesson, Grade

def student_grade_view(request):
    # Retrieve grades for the current student
    student_grades = Grade.objects.filter(student=request.user)
    return render(request, 'student_grade.html', {'student_grades': student_grades})

def lesson_detail_view(request, lesson_id):
    # Retrieve lesson details
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})
