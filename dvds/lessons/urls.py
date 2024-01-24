from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pricing/', views.pricing, name='pricing'),
    path('automatic_lessons/', views.automatic, name='auto'),
    path('instructor_training/', views.instructor, name='instructor'),
    path('intensive_courses/', views.intensive, name='intensive'),
    path('refresher_lessons/', views.refresher, name='refresher'),
    path('theory_driving_test/', views.theory_test, name='theory_test'),
    path('weekly_lessons/', views.weekly, name='weekly'),
]
