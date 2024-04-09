from django.urls import path

from . import teacherView, studentView, parentView
from . import views

urlpatterns = [
    path('grades/', views.student_grade_view, name='student_grades'),
    path('lesson/<int:lesson_id>/', views.lesson_detail_view, name='lesson_detail'),
    path('contact', views.contact, name="contact"),
    path('login', views.user_login, name="login"),
    path('logout_user', views.logout_user, name="logout_user"),

    path('student_home/', studentView.student_home, name="student_home"),

    path('teacher_home/', teacherView.teacher_home, name="teacher_home"),
    path('create_exam/', views.create_exam, name='create_exam'),
    path('create_test/', views.create_test, name='create_test'),
    path('post_grade/', views.post_grade, name='post_grade'),
    path('post_attendance/', views.post_attendance, name='post_attendance'),

    path('parent_home/', parentView.parent_page, name='parent_page'),
        

]
