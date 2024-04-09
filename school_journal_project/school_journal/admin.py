from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Lesson, Grade, Exam, Test, Attendance, Teacher, Parent, Student


# Register your models here.
# class UserModel(UserAdmin):
#     pass
#
#
# admin.site.register(UserProfile, UserModel)

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Lesson)
admin.site.register(Grade)
admin.site.register(Exam)
admin.site.register(Test)
admin.site.register(Attendance)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Student)
