from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'metainfo', views.MetaInfoViewset)
router.register(r'division', views.DivisionViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('departments/', views.set_deparment_and_college),
    path('', include(router.urls)),
]
