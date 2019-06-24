from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import StudentInfo
from app_common_data.models import MetaDatainfo
from allauth.socialaccount.models import SocialAccount

# Create your views here.

def get_student_by_major(pk):
    student = None
    try :
        student = StudentInfo.objects.get(pk=pk, student_major_division='주전공')
    except StudentInfo.DoesNotExist:
        return None
    return student

@login_required
def Student(request):
    if request.method == 'POST':
        # 데이터 가져오기
        # 대학
        university = request.POST.get('university')
        # 복수전공
        multiple_department = request.POST.get('multiple_department')
        multiple_department_college = None
        # 부전공
        sub_department = request.POST.get('sub_department')
        sub_department_college = None
        # 입학년도
        admission_year = request.POST.get('admission_year')
        # 주전공
        department = MetaDatainfo.objects.get(meta_data_relation_code=request.POST.get('department'))
        department_college = MetaDatainfo.objects.get(meta_data_relation_code=department.upper_data_code)

        # 데이터 저장
        # 주전공
        studentInfo = StudentInfo(user_id=request.user.id,
                                  student_admission_year=admission_year,
                                  student_university_name=university,
                                  student_major_division='주전공',
                                  student_name=request.user.username,
                                  student_major_name=department.meta_data_relation_name,
                                  student_college_name=department_college.meta_data_relation_name
                                  )
        studentInfo.save()

        # 복수전공
        if multiple_department != '0':
            # 복수전공 데이터 가져오기
            multiple_department = MetaDatainfo.objects.get(meta_data_relation_code=request.POST.get('multiple_department'))
            multiple_department_college = MetaDatainfo.objects.get(meta_data_relation_code=multiple_department.upper_data_code)

            studentInfo = StudentInfo(user_id=request.user.id,
                                  student_admission_year=admission_year,
                                  student_university_name=university,
                                  student_major_division='복수전공',
                                  student_name=request.user.username,
                                  student_major_name=multiple_department.meta_data_relation_name,
                                  student_college_name=multiple_department_college.meta_data_relation_name
                                  )
            studentInfo.save()

        if sub_department != '0':
            # 부전공 데이터 가져오기
            sub_department = MetaDatainfo.objects.get(meta_data_relation_code=request.POST.get('sub_department'))
            sub_department_college = MetaDatainfo.objects.get(meta_data_relation_code=sub_department.upper_data_code)
            studentInfo = StudentInfo(user_id=request.user.id,
                                  student_admission_year=admission_year,
                                  student_university_name=university,
                                  student_major_division='복수전공',
                                  student_name=request.user.username,
                                  student_major_name=sub_department.meta_data_relation_name,
                                  student_college_name=sub_department_college.meta_data_relation_name
                                  )
            studentInfo.save()

        return HttpResponse(status=204)

    '''
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