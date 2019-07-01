from django.shortcuts import render, redirect
from .models import archieving_history
from app_university_data.views import get_subject_data
from django.http import HttpResponse
from rest_framework import viewsets
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import HistorySerializer, RuleSerializer, GroupSerializer, MappingSerializer, GroupAndMappingSerializer
from django.http import Http404
from .models import archieving_history, graduation_rule, graduation_subject_group, graduation_subject_group_mapping

# Create your views here.

class HistoryViewset(viewsets.ModelViewSet):
    queryset = archieving_history.objects.all()
    serializer_class = HistorySerializer

    def get_queryset(self):
        return archieving_history.objects.filter(history_user=self.request.user.id)

class RuleViewset(viewsets.ModelViewSet):
    queryset = graduation_rule.objects.all()
    serializer_class = RuleSerializer

    def get_queryset(self):
        university_name = self.request.query_params.get('university_name')
        department_code = self.request.query_params.get('department_code')
        admission_year = self.request.query_params.get('admission_year')
        track = self.request.query_params.get('track')
        # PATCH 용
        if university_name is None:
            return graduation_rule.objects.all()
        return graduation_rule.objects.filter(rule_university_name=university_name, rule_department_code=department_code,
                                              rule_admission_year=admission_year, rule_track=track)

class GroupAndMappingViewset(viewsets.ModelViewSet):
    queryset = graduation_subject_group.objects.all()
    serializer_class = GroupAndMappingSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id')
        if id is None:
            return graduation_subject_group.objects.all()
        return graduation_subject_group.objects.filter(pk=id)

class GroupViewset(viewsets.ModelViewSet):
    queryset = graduation_subject_group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        university_name = self.request.query_params.get('university_name')
        if university_name is None:
            return graduation_subject_group.objects.all()
        return graduation_subject_group.objects.filter(subject_group_university_name=university_name)

class MappingViewset(viewsets.ModelViewSet):
    queryset = graduation_subject_group_mapping.objects.all()
    serializer_class = MappingSerializer


    def get_queryset(self):
        mapping_subject_group = self.request.query_params.get('mapping_subject_group')
        if mapping_subject_group is None:
            return graduation_subject_group_mapping.objects.all()
        return graduation_subject_group_mapping.objects.filter(mapping_subject_group=mapping_subject_group)

def save_subject(request):

    university_name = request.POST['university']
    history_lecture_code = request.POST['history_lecture_code']
    history_subject_code = request.POST['history_subject_code']
    history_subject_complete_division = request.POST['history_subject_complete_division']
    history_student_grade = request.POST['history_student_grade']
    history_grade_year = request.POST['history_grade_year']
    history_semester = request.POST['history_semester']

    # 과목 정보 가져오기
    subject = get_subject_data(university_name, history_subject_code)

    history_subject = archieving_history(history_user=request.user,
                                            history_subject_code = subject.subject_code,
                                            history_lecture_code = history_lecture_code,
                                            history_subject_name = subject.subject_name,
                                            history_subject_complete_division = history_subject_complete_division,
                                            history_subject_area = subject.subject_area,
                                            history_subject_credit = subject.subject_credit,
                                            history_subject_assessment_Methods = '',
                                            history_student_grade = history_student_grade,
                                            history_grade_year = history_grade_year,
                                            history_semester = history_semester)

    history_subject.save()
    return HttpResponse(status=204)

def mapping_save(request):
    group_name = request.POST['group_name']
    university_name = request.POST['university_name']
    divisions = request.POST.getlist('divisions[]')
    areas = request.POST.getlist('areas[]')

    #그룹 생성
    group = graduation_subject_group(
        subject_group_name=group_name,
        subject_group_university_name=university_name
    )
    group.save()

    #매핑 데이터 생성
    for i in range(len(divisions)):
        mapping = graduation_subject_group_mapping(
            mapping_subject_group=group,
            mapping_completion_division = divisions[i]
        )
        mapping.save()

    for i in range(len(areas)):
        mapping = graduation_subject_group_mapping(
            mapping_subject_group=group,
            mapping_area = areas[i]
        )
        mapping.save()

    return HttpResponse(status=204)

def mapping_update(request):
    if request.method == "POST":
        id = request.POST['id']
        group_name = request.POST['group_name']
        university_name = request.POST['university_name']
        divisions = request.POST.getlist('divisions[]')
        areas = request.POST.getlist('areas[]')

        #그룹 수정
        group = graduation_subject_group.objects.get(pk=id)
        group.subject_group_name = group_name
        group.save()

        #매핑 수정
        #먼저 모든 매핑 삭제
        mappings = graduation_subject_group_mapping.objects.filter(mapping_subject_group=group).delete()

        # 매핑 데이터 생성
        for i in range(len(divisions)):
            mapping = graduation_subject_group_mapping(
                mapping_subject_group=group,
                mapping_completion_division=divisions[i]
            )
            mapping.save()

        for i in range(len(areas)):
            mapping = graduation_subject_group_mapping(
                mapping_subject_group=group,
                mapping_area=areas[i]
            )
            mapping.save()


        return HttpResponse(status=204)

    return HttpResponse(status=400)




