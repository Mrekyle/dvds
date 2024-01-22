from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-conditions/', views.terms, name='terms'),
]
