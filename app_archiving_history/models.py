from django.db import models

# Create your models here.

# 보관기록
class archving_history(models.Model):

    # 유저아이디
    # 교과목 코드
    # 강의 코드
    # 교과목 이름
    # 교과목 이수구분
    # 교과목 영역
    # 교과목 학점
    # 교과목 평가 방법

    history_user_id = models.CharField(max_length=20)
    history_subject_code = models.CharField(max_length=20)
    history_lecture_code = models.CharField(max_length=20)
    history_subject_name = models.CharField(max_length=20)
    history_subject_complete_division = models.CharField(max_length=20)
    history_subject_area = models.CharField(max_length=20)
    history_subject_credit = models.CharField(max_length=20)
    history_subject_assessment_Methods = models.CharField(max_length=20)
