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
    history_subject_code = models.CharField(max_length=50)
    history_lecture_code = models.CharField(max_length=50)
    history_subject_name = models.CharField(max_length=50)
    history_subject_complete_division = models.CharField(max_length=50)
    history_subject_area = models.CharField(max_length=20)
    history_subject_credit = models.CharField(max_length=20)
    history_subject_assessment_Methods = models.CharField(max_length=20)
    history_student_grade = models.CharField(max_length=20)
    history_grade_year = models.CharField(max_length=20)
    history_semester = models.CharField(max_length=20)

# 졸업 요건
class graduation_rule(models.Model):
    # 대학이름
    # 학과코드
    # 입학년도
    # 졸업 요건 이름
    # 트랙
    # 룰 타입
    # 룰 값
    # 과목그룹
    rule_university_name = models.CharField(max_length=50)
    rule_department_code = models.CharField(max_length=50)
    rule_admission_year = models.CharField(max_length=20)
    rule_name = models.CharField(max_length=50)
    rule_track = models.CharField(max_length=50, default='자동')
    rule_type = models.CharField(max_length=10, default='0')
    rule_value = models.CharField(max_length=50, default='0')
    rule_subject_group = models.CharField(max_length=30)

# 과목 그룹
class graduation_subject_group(models.Model):
    # 과목 그룹 이름
    # 대학 이름
    subject_group_name = models.CharField(max_length=50)
    subject_group_university_name = models.CharField(max_length=50)

# 과목 그룹 매핑
class graduation_subject_group_mapping(models.Model):
    # 과목 그룹 번호
    # 이수 구분 명
    # 영역 명
    mapping_subject_group = models.ForeignKey(graduation_subject_group, on_delete=models.CASCADE)
    mapping_completion_division = models.CharField(max_length=50, blank=True)
    mapping_area = models.CharField(max_length=50, blank=True)