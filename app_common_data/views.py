from django.shortcuts import render
from .models import UniversityInfo, CollegeInfo, DepartmentInfo, CompletionDivision
from django.http import HttpResponse, JsonResponse
from .serializers import UniversitySerializer, DepartmentSerializer, CompletionDivisionSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

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


def get_all_UniversityInfo(request):
    if request.method == 'POST':
        #모든 대학 정보 던져주기
        Universitys = UniversityInfo.objects.all().distinct()
        return JsonResponse()
    return

