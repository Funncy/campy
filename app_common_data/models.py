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
    # 학과 이름
    university_name = models.CharField(max_length=20)
    college_name = models.CharField(max_length=20)

# 학과정보
class DepartmentInfo(models.Model):

    # 대학 이름
    # 단과대학 이름
    # 학과 이름
    university_name = models.CharField(max_length=20)
    college_name = models.CharField(max_length=20)
    department_name = models.CharField(max_length=20)

# 교과목정보
class SubjectInfo(models.Model):

    # 대학 이름
    # 단과대학 이름
    # 학과 이름
    # 교과목 이름
    university_name = models.CharField(max_length=20)
    college_name = models.CharField(max_length=20)
    department_name = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=20)