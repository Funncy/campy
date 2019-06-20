from django.db import models

# Create your models here.

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