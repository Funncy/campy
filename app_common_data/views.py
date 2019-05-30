from django.shortcuts import render
from .models import UniversityInfo, CollegeInfo, DepartmentInfo, SubjectInfo
from django.http import HttpResponse, JsonResponse
from .serializers import UniversitySerializer
from rest_framework import viewsets

# Create your views here.

class UniversityViewset(viewsets.ModelViewSet):
    queryset = UniversityInfo.objects.all()
    serializer_class = UniversitySerializer


def get_all_UniversityInfo(request):
    if request.method == 'POST':
        #모든 대학 정보 던져주기
        Universitys = UniversityInfo.objects.all().distinct()
        return JsonResponse()
    return

