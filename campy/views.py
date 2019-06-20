from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from app_account_management.models import StudentInfo
from django.contrib.auth.decorators import login_required
from django.urls import reverse

## 실 사용 list

def get_student_data(request):
    student = StudentInfo.objects.filter(pk=request.user.id, student_major_division='주전공')
    context = {
        'student': student,
    }
    return context

def index(request):
    return render(request, 'index.html', {})

# 최초 화면
def campy_info(request):
    context = get_student_data(request)
    return render(request, 'campy-info.html', context)

# 로그인 화면
def login(request):
    return render(request, 'login.html', {})

# 로그아웃 화면
def logout(request):
    return render(request, 'index.html', {})

# 최초 로그인시 계정 정보 입력
def join(request):
    student = StudentInfo.objects.filter(pk=request.user.id, student_major_division='주전공')
    context = {
        'student': student,
    }
    return render(request, 'join.html', {})

# 졸업 진단 화면
def graduation_diagnosis(request):
    student = StudentInfo.objects.filter(pk=request.user.id, student_major_division='주전공')
    context = {
        'student': student,
        'graduationActive': 1,
    }
    return render(request, 'graduation-diagnosis.html', context)

# 커뮤니티 화면
def community(request):
    student = StudentInfo.objects.filter(pk=request.user.id, student_major_division='주전공')
    context = {
        'student': student,
        'communityActive': 1,
    }
    return render(request, 'community.html', context)

# 수강 설계 화면
def course(request):
    student = StudentInfo.objects.filter(pk=request.user.id, student_major_division='주전공')
    context = {
        'student': student,
        'courseActive': 1,
    }
    return render(request, 'course-design.html', context)

# 개인정보 화면
def mypage(request):
    student = StudentInfo.objects.filter(pk=request.user.id, student_major_division='주전공')
    context = {
        'student': student,
        'mypageActive': 1,
    }
    return render(request, 'mypage.html', context)

# 개인 수강 이력 화면
def history(request):
    student = StudentInfo.objects.filter(pk=request.user.id, student_major_division='주전공')
    context = {
        'student': student,
        'historyActive': 1,
    }
    return render(request, 'history.html', context)

@login_required
def join(request):

    if request.method == 'GET':
        #StudentInfo가 없을시 최초 로그인
        if request.user.is_staff is True:
            return redirect(reverse('index'))
        try:
            student_info = StudentInfo.objects.filter(user_id=request.user.id)
        except StudentInfo.DoesNotExist:
            return render(request, 'join.html', {})

        #Studentinfo가 있을경우 메인화면으로 이동
        return redirect(reverse('index'))
    return


## 예비 list
'''
def department_manage(request):
    return render(request, 'department-manage.html', {})

def university_setting(request):
    return render(request, 'university-setting.html', {})

def subject_manage(request):
    return render(request, 'subject-manage.html', {})

def subject_groups_set(request):
    return render(request, 'subject-groups-set.html', {})

def graduation_requirements_set(request):
    return render(request, 'graduation-requirements-set.html', {})

def register(request):
    return render(request, 'register.html', {})

def test(request):
    return render(request, 'test.html', {})

def abeek(request):
    return render(request, 'abeek.html', {})

def certification(request):
    return render(request, 'certification.html', {})

def error(request):
    return render(request, 'error.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def general_settings(request):
    return render(request, 'general_settings.html', {})

def group(request):
    return render(request, 'group.html', {})

def assessment(request):
    return render(request, 'assessment.html', {})

def judge_list(request):
    return render(request, 'judge_list.html', {})


def notice(request):
    return render(request, 'notice.html', {})

def report(request):
    return render(request, 'report.html', {})

def rule(request):
    return render(request, 'rule.html', {})

def simulation(request):
    return render(request, 'simulation.html', {})

def student_data(request):
    return render(request, 'student_data.html', {})

def student_data_list(request):
    return render(request, 'student_data_list.html', {})

def student_data_upload(request):
    return render(request, 'student_data_upload.html', {})

def subject(request):
    return render(request, 'subject.html', {})

def welcome(request):
    return render(request, 'welcome.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

def notice(request):
    return render(request, 'notice.html', {})

def test_data(request):
    return HttpResponse('true')

def connect(request):
    if request.method == "POST":
        # form = LoginForm(request.POST)
        username = request.POST['userId']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    return HttpResponse()

def urls(request,url_info):
    # print(url_info)
    # url 분석
    url_data = str(url_info).split('/')
    # url 마지막 문자열을 화면명
    screen_file = url_data[len(url_data)-1]
    # 잘못된 url일 경우
    if screen_file == '':
        screen_file = '404'
    # 첫 페이지
    if url_info == '':
        screen_file = 'index'
    return render(request, screen_file+".html", {})
'''