from django.shortcuts import render
from django.utils.timezone import now
from .models import Student, Attendance, Exam, Grade, UserProfile


def student_home(request):
    user_profile = UserProfile.objects.get(user=request.user)
    student_obj = Student.objects.get(admin=user_profile)

    total_attendance = Attendance.objects.filter(student_id=student_obj).count()
    attendance_present = Attendance.objects.filter(student_id=student_obj, status=Attendance.PRESENT).count()
    attendance_absent = Attendance.objects.filter(student_id=student_obj, status=Attendance.ABSENT).count()
    grades = Grade.objects.filter(student_id=student_obj).all()

    exams_list = Exam.objects.filter(date__gte=now().date())
    upcoming_exams = []

    for l in student_obj.lessons.all():
        exam = exams_list.objects.get(lesson=l.id)
        if exam is not None:
            single_course = (l.name, exam.date)
            upcoming_exams.append(single_course)

    context = {
        "total_attendance": total_attendance,
        "attendance_present": attendance_present,
        "attendance_absent": attendance_absent,
        "upcoming_exams": upcoming_exams,
        "grades": grades,
        "student": student_obj
    }
    return render(request, "student_page.html", context)
