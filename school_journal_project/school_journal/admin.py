from django.contrib import admin
from .models import UserProfile, Lesson, URL, Grade, Exam, Test, Attendance

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Lesson)
admin.site.register(URL)
admin.site.register(Grade)
admin.site.register(Exam)
admin.site.register(Test)
admin.site.register(Attendance)
