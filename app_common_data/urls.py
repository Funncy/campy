from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'metainfo', views.MetaInfoViewset)
router.register(r'university/data', views.UniversityDataViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('departments/name/', views.set_deparment_and_college_by_name),
    path('departments/', views.set_deparment_and_college_by_code),
]
