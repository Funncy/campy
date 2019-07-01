from django.shortcuts import render
from .models import MetaDatainfo
from django.http import HttpResponse, JsonResponse
from .serializers import MetaInfoSerializer, MetaCodeSerializer, MetaRelationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.core import serializers

# Create your views here.

class MetaInfoViewset(viewsets.ModelViewSet):
    queryset = MetaDatainfo.objects.all()
    serializer_class = MetaInfoSerializer

    def get_queryset(self):
        meta_data_code = self.request.query_params.get('meta_data_code')
        upper_data_code = self.request.query_params.get('upper_data_code')
        if meta_data_code is None and upper_data_code is None:
            return MetaDatainfo.objects.all()
        return MetaDatainfo.objects.filter(meta_data_code=meta_data_code, upper_data_code=upper_data_code)

class MetaCodeViewset(viewsets.ReadOnlyModelViewSet):
    queryset = MetaDatainfo.objects.filter().values('meta_data_code', 'meta_data_name').order_by('meta_data_code').distinct()
    serializer_class = MetaCodeSerializer

class MetaRelationViewset(viewsets.ReadOnlyModelViewSet):
    queryset = MetaDatainfo.objects.filter().values('meta_data_relation_code', 'meta_data_relation_name').order_by('meta_data_relation_code').distinct()
    serializer_class = MetaRelationSerializer

class UniversityDataViewset(viewsets.ReadOnlyModelViewSet):
    queryset = MetaDatainfo.objects.all()
    serializer_class = MetaInfoSerializer

    def get_queryset(self):
        # 소속 대학 정보 가져오기
        university = self.request.query_params.get('university')
        university = MetaDatainfo.objects.get(meta_data_relation_name=university, meta_data_code='meta_universityList')
        return MetaDatainfo.objects.filter(meta_data_code=self.request.query_params.get('meta_data_code'), upper_data_code=university.meta_data_relation_code)

def set_deparment_and_college_by_name(request):
    # request데이터 가져오기
    # 상위대학 코드
    meta_data_name = request.GET['meta_data_code']
    university_code = MetaDatainfo.objects.get(meta_data_code='meta_universityList', meta_data_relation_name=meta_data_name)

    colleges = MetaDatainfo.objects.filter(upper_data_code=university_code.meta_data_relation_code, meta_data_code='meta_collegeList')

    colleges_and_departments = list()
    i = 0
    for college in colleges:
        departments = MetaDatainfo.objects.filter(upper_data_code=college.meta_data_relation_code).values(
            'meta_data_relation_name', 'meta_data_relation_code')
        print(departments)
        colleges_and_departments.append({'college_name': college.meta_data_relation_name})

        colleges_and_departments[i]['departments'] = list()
        department_count = 0
        for department in departments:
            print(department)
            print(department['meta_data_relation_name'])
            colleges_and_departments[i]['departments'].append({'department_code': department['meta_data_relation_code'],
                                                               'department_name': department[
                                                                   'meta_data_relation_name']})
            department_count += 1
            # colleges_and_departments[college.meta_data_relation_name].append(department['meta_data_relation_name'])
        colleges_and_departments[i]['counts'] = department_count
        i = i + 1

    print(colleges_and_departments)

    return JsonResponse(colleges_and_departments, safe=False)

#리펙토링 필요
def set_deparment_and_college_by_code(request):
    #request데이터 가져오기
    # 상위대학 코드
    meta_data_code = request.GET['meta_data_code']

    colleges = MetaDatainfo.objects.filter(upper_data_code=meta_data_code, meta_data_code='meta_collegeList')

    colleges_and_departments = list()
    i = 0
    for college in colleges:
        departments = MetaDatainfo.objects.filter(upper_data_code=college.meta_data_relation_code).values('meta_data_relation_name', 'meta_data_relation_code')
        print(departments)
        colleges_and_departments.append({ 'college_name' : college.meta_data_relation_name })

        colleges_and_departments[i]['departments'] = list()
        department_count = 0
        for department in departments:
            print(department)
            print(department['meta_data_relation_name'])
            colleges_and_departments[i]['departments'].append({ 'department_code' : department['meta_data_relation_code'] , 'department_name': department['meta_data_relation_name'] })
            department_count += 1
            # colleges_and_departments[college.meta_data_relation_name].append(department['meta_data_relation_name'])
        colleges_and_departments[i]['counts'] = department_count
        i = i+1

    print(colleges_and_departments)

    return JsonResponse(colleges_and_departments, safe=False)

def get_all_universitys():
    return MetaDatainfo.objects.filter(meta_data_code='meta_universityList')

