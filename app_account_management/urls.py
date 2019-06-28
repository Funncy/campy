from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'read', views.StudentInfoViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('student/', views.Student, name='student'),
    path('read2/', views.read_studentInfo, name='read_student'),
    path('privacy-update/', views.update_studentInfo, name='update_studentinfo')
]