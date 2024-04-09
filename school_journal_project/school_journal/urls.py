from django.urls import path
from . import views
from . import studentView

urlpatterns = [
    path('grades/', views.student_grade_view, name='student_grades'),
    path('lesson/<int:lesson_id>/', views.lesson_detail_view, name='lesson_detail'),
    path('contact', views.contact, name="contact"),
    path('login', views.user_login, name="login"),
    path('logout_user', views.logout_user, name="logout_user"),

    path('student_home/', studentView.student_home, name="student_home"),

]
