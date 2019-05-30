from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# 계정관리
# Create your models here.


# 학생정보
class StudentInfo(models.Model):

    # 사용자 ID
    # 학생 이름
    # 학생 입학 연도
    # 학생 전공 구분
    # 학생 전공 이름
    # 학생 단과대학 이름

    user_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=20)
    student_admission_year = models.CharField(max_length=20)
    student_major_division = models.CharField(max_length=20)
    student_major_name = models.CharField(max_length=20)
    student_college_name = models.CharField(max_length=20)
