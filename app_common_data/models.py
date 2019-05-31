from django.db import models

# Create your models here.
# 대학정보
class UniversityInfo(models.Model):

    # 대학 이름
    university_name = models.CharField(max_length=20)

# 단과대학정보
class CollegeInfo(models.Model):

    # 대학 이름
    # 단과대학 이름
    university_name = models.CharField(max_length=20)
    college_name = models.CharField(max_length=20)

# 학과정보
class DepartmentInfo(models.Model):

    # 대학 이름
    # 단과대학 이름
    # 학과 이름
    university = models.ForeignKey(UniversityInfo, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=20)
    college_name = models.CharField(max_length=20)
    department_name = models.CharField(max_length=20)

# 교과목정보
class SubjectInfo(models.Model):

    # 대학 이름
    # 교과목 코드
    # 교과목 이름
    # 교과목 이수구분
    # 교과목 영역
    # 교과목 학점
    # 교과목 평가 방법

    university_name = models.CharField(max_length=20)
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=20)
    subject_complete_division = models.CharField(max_length=20)
    subject_area = models.CharField(max_length=20)  #수정
    subject_credit = models.CharField(max_length=20)
    subject_assessment_Methods = models.CharField(max_length=20)