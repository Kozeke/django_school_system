from django.shortcuts import render
from django.utils.timezone import now
from .models import Lesson, Exam, Grade, Attendance, Teacher, UserProfile, Test
from django.db.models import Q
from django.db import models


def teacher_home(request):
    user_profile = UserProfile.objects.get(user=request.user)
    teacher = Teacher.objects.get(admin=user_profile)

    lessons = Lesson.objects.filter(teacher=teacher)
    tests = Test.objects.filter(lesson__in=lessons)
    exams = Exam.objects.filter(lesson__in=lessons)
    grades = Grade.objects.filter(exam__in=exams) | Grade.objects.filter(test__in=tests)
    attendances = Attendance.objects.filter(lesson__in=lessons)

    lesson_grades = {}
    for lesson in lessons:
        lesson_exams = exams.filter(lesson=lesson)
        lesson_tests = tests.filter(lesson=lesson)
        lesson_grades[lesson.name] = Grade.objects.filter(
            models.Q(exam__in=lesson_exams) | models.Q(test__in=lesson_tests)
        )

    upcoming_exams = exams.filter(date_time__gte=now())
    upcoming_tests = tests.filter(date_time__gte=now())
    # Get analysis of the class
    class_analysis = {}
    if grades:
        class_analysis = {
            "best_student": max(grades, key=lambda x: x.grade).student,
            "worst_student": min(grades, key=lambda x: x.grade).student,
            "average_grade": sum(grade.grade for grade in grades) / len(grades),
        }

    context = {
        "teacher": teacher,
        "lessons": lessons,
        "exams": exams,
        "tests": tests,
        "grades": grades,
        "attendances": attendances,
        "lesson_grades": lesson_grades,
        "upcoming_exams": upcoming_exams,
        "upcoming_tests": upcoming_tests,
        "class_analysis": class_analysis,
    }

    return render(request, "teacher_page.html", context)
