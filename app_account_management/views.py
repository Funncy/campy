from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import StudentInfo
from app_common_data.models import UniversityInfo, DepartmentInfo
from allauth.socialaccount.models import SocialAccount

# Create your views here.

@login_required
def join(request):

    if request.method == 'GET':
        #StudentInfo가 없을시 최초 로그인
        if request.user.is_staff is True:
            return redirect(reverse('index'))
        try:
            student_info = StudentInfo.objects.get(user_id=request.user.id)
        except StudentInfo.DoesNotExist:
            return render(request, 'join.html', {})

        #Studentinfo가 있을경우 메인화면으로 이동
        return redirect(reverse('index'))
    return

@login_required
def Student(request):
    if request.method == 'POST':
        #studentInfo 저장
        #user = request.user
        print('test')
        #print(request.POST.get('university'))
        print(request.user.username)
        departmentInfo = DepartmentInfo.objects.get(pk=request.POST.get('department'))
        studentInfo = StudentInfo(user_id=request.user.id,
                                  student_admission_year=request.POST.get('admission_year'),
                                  student_university_name=departmentInfo.university_name,
                                  student_major_division='주전공',
                                  student_name=request.user.username,
                                  student_major_name=departmentInfo.department_name,
                                  student_college_name=departmentInfo.college_name
                                  )
        studentInfo.save()
        return HttpResponse()
    return HttpResponse()