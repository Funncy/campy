from django.shortcuts import render
from .models import UniversityInfo, CollegeInfo, DepartmentInfo, SubjectInfo
from django.http import HttpResponse, JsonResponse
from .serializers import UniversitySerializer, DepartmentSerializer, SubjectSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class SubjectsViewset(viewsets.ModelViewSet):
    queryset = SubjectInfo.objects.all()
    serializer_class = SubjectSerializer

class UniversityViewset(viewsets.ModelViewSet):
    queryset = UniversityInfo.objects.all()
    serializer_class = UniversitySerializer

class DepartmentViewset(viewsets.ModelViewSet):
    queryset = DepartmentInfo.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        university = self.request.query_params.get('university')
        return DepartmentInfo.objects.filter(university=university)

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

