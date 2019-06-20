from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 보관기록
class archieving_history(models.Model):
    # 유저아이디
    # 교과목 코드
    # 강의 코드 (잠시 보류)
    # 교과목 이름
    # 교과목 이수구분
    # 교과목 영역
    # 교과목 학점
    # 교과목 평가 방법 (잠시 보류)
    # 학생 성적
    # 이수 학년
    # 이수 학기
    history_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    history_subject_code = models.CharField(max_length=20)
    history_lecture_code = models.CharField(max_length=20)
    history_subject_name = models.CharField(max_length=20)
    history_subject_complete_division = models.CharField(max_length=20)
    history_subject_area = models.CharField(max_length=20)
    history_subject_credit = models.CharField(max_length=20)
    history_subject_assessment_Methods = models.CharField(max_length=20)
    history_student_grade = models.CharField(max_length=20)
    history_grade_year = models.CharField(max_length=20)
    history_semester = models.CharField(max_length=20)

