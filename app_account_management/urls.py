from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('student/', views.Student, name='student'),
]