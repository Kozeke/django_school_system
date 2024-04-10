from django.shortcuts import render
from django.utils.timezone import now
from .models import Student, Attendance, Exam, Grade, UserProfile, Test


def student_home(request):
    user_profile = UserProfile.objects.get(user=request.user)
    student_obj = Student.objects.get(admin=user_profile)

    total_attendance = Attendance.objects.filter(student_id=student_obj).count()
    attendance_present = Attendance.objects.filter(student_id=student_obj, status=Attendance.PRESENT).count()
    attendance_absent = Attendance.objects.filter(student_id=student_obj, status=Attendance.ABSENT).count()
    grades = Grade.objects.filter(student_id=student_obj).all()

    lessons = student_obj.lessons.all()
    upcoming_exams = []
    upcoming_tests = []

    for lesson in lessons:
        exams = Exam.objects.filter(lesson=lesson, date_time__gte=now().date())
        if exams.exists():
            upcoming_exams.extend([(lesson.name, exam.date_time) for exam in exams])

        tests = Test.objects.filter(lesson=lesson, date_time__gte=now().date())
        if tests.exists():
            upcoming_tests.extend([(lesson.name, test.date_time) for test in tests])

    context = {
        "total_attendance": total_attendance,
        "attendance_present": attendance_present,
        "attendance_absent": attendance_absent,
        "upcoming_exams": upcoming_exams,
        "upcoming_tests": upcoming_tests,
        "grades": grades,
        "student": student_obj
    }
    return render(request, "student_page.html", context)
