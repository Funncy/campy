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

# 학교별 이수구분
class CompletionDivision(models.Model):

    # 대학
    # 대학 이름
    # 이수 구분 명
    university = models.ForeignKey(UniversityInfo, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=20)
    completion_division_name = models.CharField(max_length=20)

# 학교별 과목영역
class SubjectDomain(models.Model):

    # 대햑
    # 대학 이름
    # 도메인 이름
    university = models.ForeignKey(UniversityInfo, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=20)
    domain_name = models.CharField(max_length=20)


# 메타데이터정보
class MetaDatainfo(models.Model):
    # 메타 데이터 코드
    # 메타 데이터 이름
    # 메타 관련 데이터 코드
    # 메타 관련 데이터 이름
    # 상위 데이터 코드
    # 메타 데이터 생성 일자

    meta_data_code = models.CharField(max_length=50)
    meta_data_name = models.CharField(max_length=50)
    meta_data_relation_code = models.CharField(max_length=50)
    meta_data_relation_name = models.CharField(max_length=50)
    upper_data_code = models.CharField(max_length=50, blank=True)
    # meta_data_creation_date = models.DateTimeField(auto_now_add=True)

