from django.db import models

# Create your models here.

# 교과목정보
class SubjectInfo(models.Model):

    # 대학 이름
    # 교과목 코드
    # 교과목 이름
    # 교과목 이수구분
    # 교과목 영역
    # 교과목 학점
    university_name = models.CharField(max_length=20)
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=20)
    subject_completion_division = models.CharField(max_length=20)
    subject_area = models.CharField(max_length=20, blank=True)
    subject_credit = models.FloatField()


# 강의일정
class LectureCalendar(models.Model):
    # 강의 코드
    # 강의 교과목 코드
    # 강의 교과목 이름
    # 강의 교수님 이름
    # 강의 장소
    # 강의 요일
    # 강의 시작 시간
    # 강의 종료 시간
    # 강의 개설 년도
    # 강의 개설 학기
    # 강의 개설 학과

    lecture_code = models.CharField(max_length=20)
    lecture_subject_code = models.CharField(max_length=20)
    lecture_subject_name = models.CharField(max_length=20)
    lecture_professor_name = models.CharField(max_length=20)
    lecture_place = models.CharField(max_length=20)
    lecture_week_expression = models.CharField(max_length=20)
    lecture_star_time = models.CharField(max_length=20)
    lecture_end_time = models.CharField(max_length=20)
    lecture_opened_year = models.CharField(max_length=20)
    lecture_opened_semester = models.CharField(max_length=20)
    lecture_opened_department = models.CharField(max_length=20)
