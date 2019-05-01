from django.db import models

# Create your models here.

# 강의일정
class LectureCalendar(models.Model):

    # 강의 코드
    # 강의 교과목 코드
    # 강의 교과목 이름
    # 강의 선생님 이름
    # 강의 장소
    # 강의 요일
    # 강의 날짜
    # 강의 시작 시간
    # 강의 종료 시간
    # 강의 개설 년도
    # 강의 개설 학기
    # 강의 개설 학과
    
    lecture_code = models.CharField(max_length=20)
    lecture_subject_code = models.CharField(max_length=20)
    lecture_subject_name = models.CharField(max_length=20)
    lecture_teacher_name = models.CharField(max_length=20)
    lecture_place = models.CharField(max_length=20)
    lecture_week_expression = models.CharField(max_length=20)
    lecture_date = models.CharField(max_length=20)
    lecture_star_time = models.CharField(max_length=20)
    lecture_end_time = models.CharField(max_length=20)
    lecture_opened_year = models.CharField(max_length=20)
    lecture_opened_semester = models.CharField(max_length=20)
    lecture_opened_department = models.CharField(max_length=20)


# 수강설계
class CoursePlanning(models.Model):

    # 사용자 ID
    # 수강 계획 코드
    # 수강 계획 이름
    # 강의코드
    # 강의알람
    # 수강 일정 여부
    
    user_id = models.CharField(max_length=20)
    course_plan_code = models.CharField(max_length=20)
    course_plan_name = models.CharField(max_length=20)
    lecture_code = models.CharField(max_length=20)
    lecture_alarm = models.CharField(max_length=20)
    course_schedule_yn = models.CharField(max_length=20)