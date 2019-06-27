from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SubjectSerializer
from .models import SubjectInfo
from app_account_management.models import StudentInfo
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from rest_framework.pagination import PageNumberPagination

# Create your views here.

# pagination용
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SubjectsViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SubjectInfo.objects.all()
    serializer_class = SubjectSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        university = self.request.query_params.get('university')
        search = self.request.query_params.get('search')
        # Search로 들어온 값
        if search == '1':
            division = self.request.query_params.get('division')
            area = self.request.query_params.get('area')

            #대학 전체 조회
            if university == '학교 전체':
                return SubjectInfo.objects.all()
            else: #대학 내에서 이수구분 전체
                if division == '이수구분 전체':
                    if area == '영역 전체': # 대학 내부 모든 과목
                        return SubjectInfo.objects.filter(university_name=university)
                    else:
                        return SubjectInfo.objects.filter(university_name=university, subject_area=area)
                else:
                    if area == '영역 전체':
                        return SubjectInfo.objects.filter(university_name=university, subject_completion_division=division)
                    else:
                        return SubjectInfo.objects.filter(university_name=university, subject_completion_division=division, subject_area=area)
        else:
            return SubjectInfo.objects.filter(university_name=university)


class SubjectViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SubjectInfo.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        university = self.request.query_params.get('university')
        subject = self.request.query_params.get('subject')
        return SubjectInfo.objects.filter(university_name=university, subject_name=subject)

# 모든 과목 가져오기 (학생 데이터 기반)
def get_all_subject_by_student(student):
    return SubjectInfo.objects.filter(university_name=student.student_university_name)

# 모든 과목 가져오기 (관리자용)
def get_all_subject():
    return SubjectInfo.objects.all()

# 과목 정보 가져오기
def get_subject_data(university_name, subject_code):
    return SubjectInfo.objects.filter(university_name=university_name, subject_code=subject_code).first()