"""hel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    
    
    # ui list
    path('', views.campy_info),
    path('login/', views.login),
    path('dashboard/', views.dashboard),
    path('graduation-diagnosis/', views.graduation_diagnosis),
    path('notice/', views.notice),
    path('department-manage/', views.department_manage),
    path('subject-manage/', views.subject_manage),
    path('subject-groups-set/', views.subject_groups_set),
    path('graduation-requirements-set/', views.graduation_requirements_set),
    path('my-schedule/', views.my_schedule),

    # data list
    path('data-test', views.test_data),
    path('subject-manage/data-test', views.test_data),

    # redirect list
    path('index', views.campy_info),
    
]