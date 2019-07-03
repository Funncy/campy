from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'history', views.HistoryViewset)
router.register(r'rules', views.RuleViewset)
router.register(r'mappings', views.MappingViewset)
router.register(r'group/mappings', views.GroupAndMappingViewset)
router.register(r'group', views.GroupViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('subject/', views.save_subject),
    path('mapping/save/', views.mapping_save),
    path('mapping/update/', views.mapping_update),
]
