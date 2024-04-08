from django.contrib import admin
from .models import Student, Teacher, Grade, Attendance

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Grade)
admin.site.register(Attendance)
