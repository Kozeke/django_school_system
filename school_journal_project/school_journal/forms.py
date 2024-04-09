from django import forms
from .models import Exam, Test, Grade, Attendance


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['lesson', 'date_time']


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['lesson', 'date_time']


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['exam', 'test', 'student', 'grade']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'status', 'lesson', 'date']  

