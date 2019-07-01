from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    # admin list
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('accounts/', include('allauth.urls')),
    path('logout/', views.logout, name='logout'),

    # ui list
    path('', views.campy_info, name='index'),
    path('history/', views.history, name='history'),
    path('course/', views.course, name='course'),
    path('graduation/', views.graduation_diagnosis, name='graduation'),
    path('community/', views.community, name='community'),
    path('mypage/', views.mypage, name='mypage'),
    path('join/', views.join, name='join'),
    path('rule/', views.rule, name='rule'),
    path('subject/', views.subject, name='subject'),
    path('subject/group/', views.subject_group.as_view(), name='subject_group'),
    path('general/', views.general.as_view(), name='general'),
    path('general/create', views.general_create, name='general_create'),

    # data list
    path('data/user/', include('app_account_management.urls')),
    path('data/common/', include('app_common_data.urls')),
    path('data/history/', include('app_archiving_history.urls')),
    path('data/account/', include('app_account_management.urls')),
    path('data/university/', include('app_university_data.urls')),
    path('data/graduation/', include('app_graduation_diagnosis.urls')),
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