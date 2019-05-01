# import logging
# from rest_framework import viewsets
# from django.contrib.auth import login
# from django.contrib.auth.models import  Group, User
# from University.models import Subject
# from DjangoGms.serializers import *
# logging.basicConfig(filename='./log/info.log', level=logging.INFO)
# from .forms import UserForm
# import requests

from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# from .custom_auth import check_if_user


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """

#     # orm 쿼리
#     queryset = User.objects.all().order_by('-date_joined')
#     # 데이터 형식
#     serializer_class = UserSerializer

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer    

# class SubjectViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer


# class Connect(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


def index(request):
    return render(request, 'index.html', {})

def test(request):
    return render(request, 'test.html', {})

def abeek(request):
    return render(request, 'abeek.html', {})

def certification(request):
    return render(request, 'certification.html', {})

def error(request):
    return render(request, 'error.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def general_settings(request):
    return render(request, 'general_settings.html', {})

def group(request):
    return render(request, 'group.html', {})

def assessment(request):
    return render(request, 'assessment.html', {})

def judge_list(request):
    return render(request, 'judge_list.html', {})

def mypage(request):
    return render(request, 'mypage.html', {})

def notice(request):
    return render(request, 'notice.html', {})

def report(request):
    return render(request, 'report.html', {})

def rule(request):
    return render(request, 'rule.html', {})

def simulation(request):
    return render(request, 'simulation.html', {})

def student_data(request):
    return render(request, 'student_data.html', {})

def student_data_list(request):
    return render(request, 'student_data_list.html', {})
  
def student_data_upload(request):
    return render(request, 'student_data_upload.html', {})

def subject(request):
    return render(request, 'subject.html', {})

def welcome(request):
    return render(request, 'welcome.html', {})

def login(request):
    return render(request, 'login.html', {})

def connect(request):
    if request.method == "POST":
        # form = LoginForm(request.POST)
        username = request.POST['userId']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    return HttpResponse()

def logout(request):
    return render(request, 'index.html', {})

def urls(request,url_info):
    # print(url_info)
    # url 분석
    url_data = str(url_info).split('/')
    # url 마지막 문자열을 화면명
    screen_file = url_data[len(url_data)-1]
    # 잘못된 url일 경우
    if screen_file == '':
        screen_file = '404'
    # 첫 페이지
    if url_info == '':
        screen_file = 'index'
    return render(request, screen_file+".html", {})

