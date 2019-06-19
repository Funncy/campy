from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    # admin list
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('accounts/', include('allauth.urls')),

    # ui list
    path('', views.campy_info, name='index'),
    path('history/', views.history, name='history'),
    path('course/', views.course, name='course'),
    path('graduation/', views.graduation_diagnosis, name='graduation'),
    path('community/', views.community, name='community'),
    path('mypage/', views.mypage, name='mypage'),

    # api list
    path('join/', include('app_account_management.urls')),
    path('common/', include('app_common_data.urls')),
    path('history/', include('app_archiving_history.urls')),
]

''' path('', views.campy_info),
    path('login/', views.login),
    path('dashboard/', views.dashboard),
    path('graduation-diagnosis/', views.graduation_diagnosis),
    path('notice/', views.notice),
    path('department-manage/', views.department_manage),
    path('subject-manage/', views.subject_manage),
    path('subject-groups-set/', views.subject_groups_set),
    path('graduation-requirements-set/', views.graduation_requirements_set),
    path('my-schedule/', views.my_schedule),
    path('university-setting', views.university_setting),

    # data list
    path('data-test', views.test_data),
    path('subject-manage/data-test', views.test_data),

    # redirect list
    path('index', views.campy_info),'''