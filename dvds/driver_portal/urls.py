from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.driver_portal, name='student'),
    path('admin_portal', views.admin_portal, name='admin'),
    path('lesson_pricing', views.lesson_pricing, name='lesson_pricing'),
]
