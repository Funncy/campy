from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'universitys', views.UniversityViewset)
router.register(r'departments', views.DepartmentViewset)
router.register(r'subjects', views.SubjectsViewset)
router.register(r'subject', views.SubjectViewset)
router.register(r'division', views.CompletionDivisionViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
]
