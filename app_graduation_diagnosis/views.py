from django.shortcuts import render
from .models import archieving_history
from app_university_data.views import get_subject_data
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import HistorySerializer, RuleSerializer
from django.http import Http404
from .models import archieving_history, graduation_rule

# Create your views here.

class HistoryViewset(viewsets.ModelViewSet):
    queryset = archieving_history.objects.all()
    serializer_class = HistorySerializer

    def get_queryset(self):
        return archieving_history.objects.filter(history_user=self.request.user)

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

