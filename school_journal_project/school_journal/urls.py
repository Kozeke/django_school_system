from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('student/', views.student_page, name='student_page'),
    path('teacher/', views.teacher_page, name='teacher_page'),
    path('parent/', views.parent_page, name='parent_page'),
    path('', views.home_page, name='home_page'),
]
