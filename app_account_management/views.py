from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import StudentInfo
from app_common_data.models import MetaDatainfo
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
'''
@login_required
def Student(request):
    if request.method == 'POST':
        # 주전공 가져오기
        departmentInfo = DepartmentInfo.objects.get(pk=request.POST.get('department'))

        # 복수/부 전공 가져오기
        multiple_departmentInfo = None
        sub_departments = None

        if request.POST.get('multiple_department') != '0':
            multiple_departmentInfo = DepartmentInfo.objects.get(pk=request.POST.get('multiple_department'))

        if request.POST.get('sub_department') != '0':
            sub_departments = DepartmentInfo.objects.get(pk=request.POST.get('sub_department'))

        #학생정보 저장
        studentInfo = StudentInfo(user_id=request.user.id,
                                  student_admission_year=request.POST.get('admission_year'),
                                  student_university_name=departmentInfo.university_name,
                                  student_major_division='주전공',
                                  student_name=request.user.username,
                                  student_major_name=departmentInfo.department_name,
                                  student_college_name=departmentInfo.college_name
                                  )
        studentInfo.save()
        #복수 전공 있을시 복수전공 저장
        if multiple_departmentInfo is not None:
            studentInfo = StudentInfo(user_id=request.user.id,
                                      student_admission_year=request.POST.get('admission_year'),
                                      student_university_name=multiple_departmentInfo.university_name,
                                      student_major_division='복수전공',
                                      student_name=request.user.username,
                                      student_major_name=multiple_departmentInfo.department_name,
                                      student_college_name=multiple_departmentInfo.college_name
                                      )
            studentInfo.save()
        #부전공 있을시 부전공 저장
        if sub_departments is not None:
            studentInfo = StudentInfo(user_id=request.user.id,
                                      student_admission_year=request.POST.get('admission_year'),
                                      student_university_name=sub_departments.university_name,
                                      student_major_division='부전공',
                                      student_name=request.user.username,
                                      student_major_name=sub_departments.department_name,
                                      student_college_name=sub_departments.college_name
                                      )
            studentInfo.save()
        return HttpResponse()
    return HttpResponse()
'''