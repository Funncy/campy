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

# Create your views here.

class SubjectsViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SubjectInfo.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        university = self.request.query_params.get('university')
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
def get_all_subject(request, student):
    return SubjectInfo.objects.filter(university_name=student.student_university_name)

# 과목 정보 가져오기
def get_subject_data(university_name, subject_code):
    return SubjectInfo.objects.filter(university_name=university_name, subject_code=subject_code).first()