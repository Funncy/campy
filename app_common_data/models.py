from django.db import models

# Create your models here.
# 대학정보
class UniversityInfo(models.Model):

    # 대학 이름
    # 최대학점 (4.5, 4.3, 4.0)
    university_name = models.CharField(max_length=20)
    university_max_grade = models.FloatField()

# 단과대학정보 (사용 x)
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
    college_name = models.CharField(max_length=20, blank=True)
    department_name = models.CharField(max_length=20)

# 교과목정보
class SubjectInfo(models.Model):

    # 대학
    # 대학 이름
    # 교과목 코드
    # 교과목 이름
    # 교과목 이수구분
    # 교과목 영역
    # 교과목 학점
    university = models.ForeignKey(UniversityInfo, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=20)
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=20)
    subject_completion_division = models.CharField(max_length=20)
    subject_area = models.CharField(max_length=20, blank=True)
    subject_credit = models.FloatField()

# 학교별 이수구분
class CompletionDivision(models.Model):

    # 대학
    # 대학 이름
    # 이수 구분 명
    university = models.ForeignKey(UniversityInfo, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=20)
    Division_name = models.CharField(max_length=20)

# 학교별 과목영역
class SubjectDomain(models.Model):

    # 대햑
    # 대학 이름
    # 도메인 이름
    university = models.ForeignKey(UniversityInfo, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=20)
    Domain_name = models.CharField(max_length=20)
