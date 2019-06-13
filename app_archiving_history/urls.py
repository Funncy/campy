from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'subjects', views.HistoryViewset)

urlpatterns = [
    path('', include(router.urls)),
    # ui list
    path('/history', views.history),
]
