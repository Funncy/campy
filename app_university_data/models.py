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
    university_name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=50)
    subject_completion_division = models.CharField(max_length=50)
    subject_area = models.CharField(max_length=50, blank=True)
    subject_credit = models.FloatField()


# INSERT INTO app_university_data_subjectinfo (university_name,
# subject_code,
# subject_name,
# subject_completion_division,
# subject_area,
# subject_credit)
# select '세종대학교',학수번호, 교과목명,이수구분,선택영역,0 from app_data_conversion_datadumpo group by 개설대학, 학수번호, 교과목명,이수구분,선택영역;


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

    lecture_code = models.CharField(max_length=50)
    lecture_subject_code = models.CharField(max_length=50)
    lecture_subject_name = models.CharField(max_length=50)
    lecture_professor_name = models.CharField(max_length=50)
    lecture_place = models.CharField(max_length=50)
    lecture_week_expression = models.CharField(max_length=50)
    lecture_star_time = models.CharField(max_length=50)
    lecture_end_time = models.CharField(max_length=50)
    lecture_opened_year = models.CharField(max_length=50)
    lecture_opened_semester = models.CharField(max_length=50)
    lecture_opened_department = models.CharField(max_length=50)


# INSERT INTO app_university_data_lecturecalendar (
# id
# ,lecture_code
# ,lecture_subject_code
# ,lecture_subject_name
# ,lecture_professor_name
# ,lecture_place
# ,lecture_week_expression
# ,lecture_star_time
# ,lecture_end_time
# ,lecture_opened_year
# ,lecture_opened_semester
# ,lecture_opened_department)
# select id,id,학수번호,교과목명,교수명,'교실',요일,강의시작시간,강의종료시간,년도,학기,개설학과전공 from app_data_conversion_datadumpo