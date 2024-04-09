from django.urls import path
from . import views

urlpatterns = [
    path('grades/', views.student_grade_view, name='student_grades'),
    path('lesson/<int:lesson_id>/', views.lesson_detail_view, name='lesson_detail'),
]
