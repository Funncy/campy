from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# 계정관리
# Create your models here.
# 사용자정보
class UserInfo(models.Model):

#     # 사용자 ID
#     # 사용자 패스워드
#     # 사용자 이름
#     # 사용자 이메일
#     # 사용자 연락번호
#     # 사용자 권한
#     # 사용자 대학이름

     user_id = models.CharField(max_length=20)
     user_password = models.CharField(max_length=20)
     user_name = models.CharField(max_length=20)
     user_email = models.CharField(max_length=20)
     user_contact_number = models.CharField(max_length=20, null=True)
     user_privilege = models.CharField(max_length=20, null=True)
     user_university_name = models.CharField(max_length=20)

# 학생정보
class StudentInfo(models.Model):

    # 사용자 ID
    # 학생 이름
    # 학생 번호(학번)
    # 학생 입학 연도
    # 학생 전공 구분
    # 학생 전공 이름
    # 학생 대학 이름
    # 학생 단과대학 이름

    user_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=20)
    # student_number = models.CharField(max_length=20)
    student_admission_year = models.CharField(max_length=20)
    student_major_division = models.CharField(max_length=20)
    student_major_name = models.CharField(max_length=20)
    student_university_name = models.CharField(max_length=20)
    student_college_name = models.CharField(max_length=20)