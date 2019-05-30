from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.UniversityViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('universitys/', include(router.urls)),
]