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

    # path('data/account_management/', views.connect),
    # path('data/archiving_history/', views.connect),
    # path('data/course_design/', views.connect),
    # path('data/subject_management/', views.connect),
    # path('data/graduation_diagnosis/', views.connect),

    # 화면
    #naver.com -> path('', views.index)
    path('', views.index),
    path('login/', views.login),
    path('test/', views.test),

    # path('rule/create/search/group/', views.ruleCreateSearchGroup),
    # path('rule/search/department/', views.ruleCreateSearchGroup),
    
    # serializer
    # path('data/', include(routers.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # 로그인
    # path('join/', views.signup, name='join'),
    # 모든 URL
    # re_path('(?P<url_info>.*?)/$', views.urls),

]

'''
    path('admin/', admin.site.urls),
    path('user/login/', views.login),
    path('user/logout/', views.logout),
    path('login/connect/', views.connect),
    path('index/', views.index),
    path('abeek/', views.abeek),
    path('certification/', views.certification),
    path('error/', views.error),
    path('faq/', views.faq),
    path('general_settings/', views.general_settings),
    path('group/', views.group),
    path('assessment/', views.assessment),
    path('judge_list/', views.judge_list),
    path('mypage/', views.mypage),
    path('notice/', views.notice),
    path('report/', views.report),
    path('rule/', views.rule),
    path('simulation/', views.simulation),
    path('student_data/', views.student_data),
    path('student_data_list/', views.student_data_list),
    path('student_data_upload/', views.student_data_upload),
    path('subject/', views.subject),
    path('welcome/', views.welcome),


    path('data/', views.welcome),
    '''
