from django.shortcuts import render
from .models import UniversityInfo, CollegeInfo, DepartmentInfo, SubjectInfo
from django.http import HttpResponse, JsonResponse
from .serializers import UniversitySerializer, DepartmentSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class UniversityViewset(viewsets.ModelViewSet):
    queryset = UniversityInfo.objects.all()
    serializer_class = UniversitySerializer

class DepartmentViewset(viewsets.ModelViewSet):
    queryset = DepartmentInfo.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        university = self.request.query_params.get('university')
        return DepartmentInfo.objects.filter(university=university)


def get_all_UniversityInfo(request):
    if request.method == 'POST':
        #모든 대학 정보 던져주기
        Universitys = UniversityInfo.objects.all().distinct()
        return JsonResponse()
    return

