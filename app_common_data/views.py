from django.shortcuts import render
from .models import UniversityInfo, CollegeInfo, DepartmentInfo, SubjectInfo, CompletionDivision
from django.http import HttpResponse, JsonResponse
from .serializers import UniversitySerializer, DepartmentSerializer, SubjectSerializer, CompletionDivisionSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class SubjectsViewset(viewsets.ModelViewSet):
    queryset = SubjectInfo.objects.all()
    serializer_class = SubjectSerializer

class SubjectViewset(viewsets.ModelViewSet):
    queryset = SubjectInfo.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        university = self.request.query_params.get('university')
        subject = self.request.query_params.get('subject')
        return SubjectInfo.objects.filter(university_name=university, subject_name=subject)

class UniversityViewset(viewsets.ModelViewSet):
    queryset = UniversityInfo.objects.all()
    serializer_class = UniversitySerializer

    def get_queryset(self):
        university = self.request.query_params.get('university')
        return UniversityInfo.objects.filter(university_name=university)

class DepartmentViewset(viewsets.ModelViewSet):
    queryset = DepartmentInfo.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        university = self.request.query_params.get('university')
        return DepartmentInfo.objects.filter(university_name=university)

class CompletionDivisionViewset(viewsets.ModelViewSet):
    queryset = CompletionDivision.objects.all()
    serializer_class = CompletionDivisionSerializer

    def get_queryset(self):
        university = self.request.query_params.get('university')
        return CompletionDivision.objects.filter(university_name=university)

class DivisionViewset(viewsets.ModelViewSet):
    queryset = SubjectInfo.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        subject_id = self.request.query_params.get('subject_id')
        return SubjectInfo.objects.filter(id=subject_id)


def get_all_UniversityInfo(request):
    if request.method == 'POST':
        #모든 대학 정보 던져주기
        Universitys = UniversityInfo.objects.all().distinct()
        return JsonResponse()
    return

