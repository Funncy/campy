from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import StudentInfo
from app_common_data.models import MetaDatainfo
from allauth.socialaccount.models import SocialAccount
from django.core import serializers
from rest_framework import viewsets
from .serializers import StudentInfoSerializer

# Create your views here.

def get_student_by_major(pk):
    student = None
    try :
        student = StudentInfo.objects.get(user_id=pk, student_major_division='주전공')
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


class StudentInfoViewset(viewsets.ModelViewSet):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return StudentInfo.objects.filter(user_id=user_id)


    # 사용자 ID
    # 학생 이름
    # 학생 번호(학번)
    # 학생 입학 연도
    # 학생 전공 구분
    # 학생 전공 이름
    # 학생 대학 이름
    # 학생 단과대학 이름


def read_studentInfo(request):
    print('2'+str(request));
    if request.method == 'GET':
        # 조회
        parameter_userId = request.user.id #request.GET['user_id']
        studentInfo_list = StudentInfo.objects.filter(user_id=1)



        response = serializers.serialize("json", studentInfo_list)

        return HttpResponse(response, content_type='application/json')

    return HttpResponse()
