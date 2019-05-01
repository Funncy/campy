from django.db import models

# Create your models here.
# 교과목정보
class CourseInfo(models.Model):

    # 교과목 코드
    # 교과목 이름
    # 교과목 구분
    # 교과목 영역
    # 교과목 학점
    # 교과목 평가 방법

    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=20)
    subject_division = models.CharField(max_length=20)
    subject_area = models.CharField(max_length=20)
    subject_credit = models.CharField(max_length=20)
    subject_assessment_Methods = models.CharField(max_length=20)