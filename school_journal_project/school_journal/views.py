from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from .models import Lesson, Grade, UserProfile
from .forms import LoginForm, ExamForm, TestForm, GradeForm, AttendanceForm
from django.contrib import messages


def student_grade_view(request):
    # Retrieve grades for the current student
    student_grades = Grade.objects.filter(student=request.user)
    return render(request, 'student_grade.html', {'student_grades': student_grades})


def lesson_detail_view(request, lesson_id):
    # Retrieve lesson details
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})


def contact(request):
    return render(request, 'contact.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                    print(user)

                    user_profile = UserProfile.objects.get(user=user)

                    if user_profile.userType == UserProfile.STUDENT:
                        return redirect('student_home/')
                    elif user_profile.userType == UserProfile.TEACHER:
                        return redirect('teacher_home/')
                    elif user_profile.userType == UserProfile.PARENT:
                        return redirect('parent_home/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_home')  # Redirect to teacher home after successful form submission
    else:
        form = ExamForm()
    return render(request, 'create_exam.html', {'form': form})

def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_home')  # Redirect to teacher home after successful form submission
    else:
        form = TestForm()
    return render(request, 'create_test.html', {'form': form})


def post_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_home')  # Redirect to teacher home after successful form submission
    else:
        form = GradeForm()
    return render(request, 'post_grade.html', {'form': form})

def post_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_home')  # Redirect to teacher home after successful form submission
    else:
        form = AttendanceForm()
    return render(request, 'post_attendance.html', {'form': form})