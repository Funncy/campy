from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from app_account_management.models import StudentInfo
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from app_account_management.views import get_student_by_major
from app_university_data.views import get_all_subject_by_student, get_all_subject
from app_common_data.views import get_all_universitys
from django.views.generic import ListView, CreateView
from app_graduation_diagnosis.models import graduation_subject_group
from app_common_data.models import MetaDatainfo


# 화면 데이터 가져오는 함수
def get_context_data(request, activeName):
    # 학생 정보 및 활성화 메뉴 설정
    student = get_student_by_major(request.user.id)
    context = {
        'student': student,
        activeName : 1
    }
    return context

## 실 사용 list
def index(request):
    return render(request, 'index.html', {})

def test(request): 
    context = get_context_data(request, 'indexActive')
    return render(request, 'subject-group-add.html', context)

# 최초 화면
def campy_info(request):
    context = get_context_data(request, 'indexActive')
    return render(request, 'campy-info.html', context)

# 로그인 화면
def login(request):
    return render(request, 'login.html', {})

# 로그아웃 화면
def logout(request):
    return render(request, 'index.html', {})

# 최초 로그인시 계정 정보 입력
def join(request):
    context = get_context_data(request, 'joinActive')
    return render(request, 'join.html', context)

# 졸업 진단 화면
def graduation_diagnosis(request):
    context = get_context_data(request, 'graduationActive')
    return render(request, 'graduation-diagnosis.html', context)

# 커뮤니티 화면
def community(request):
    context = get_context_data(request, 'communityActive')
    return render(request, 'community.html', context)

# 수강 설계 화면
def course(request):
    context = get_context_data(request, 'courseActive')
    return render(request, 'course-design.html', context)

# 개인정보 화면
def mypage(request):
    context = get_context_data(request, 'mypageActive')
    universitys = get_all_universitys()
    context['universitys'] = universitys
    return render(request, 'mypage.html', context)

# 개인 수강 이력 화면
def history(request):
    context = get_context_data(request, 'historyActive')
    subjects = get_all_subject_by_student(context['student'])
    context['subjects'] = subjects
    return render(request, 'history.html', context)

# 룰 설정 화면
def rule(request):
    context = get_context_data(request, 'ruleActive')
    universitys = get_all_universitys()
    context['universitys'] = universitys
    return render(request, 'rule-manage.html', context)

# 과목 그룹 설정 화면
class subject_group(ListView):
    model = graduation_subject_group
    template_name = 'subject-group-manage.html'
    context_object_name = 'context'

    # search 용
    def get_queryset(self):
        try:
            university = self.request.GET['university']
        except:
            university = ''
        if university == '':
            return graduation_subject_group.objects.all()
        return graduation_subject_group.objects.filter(subject_group_university_name=university)

    # context에 대학 추가
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['universitys'] = get_all_universitys()
        return context

def subject_group_create(request):
    context = get_context_data(request, 'ruleActive')
    universitys = get_all_universitys()
    context['universitys'] = universitys
    return render(request, 'subject-group-add.html', context)

def subject_group_update(request):
    context = get_context_data(request, 'ruleActive')
    return render(request, 'subject-group-update.html', context)

# 과목 설정 화면
def subject(request):
    context = get_context_data(request, 'subjectActive')
    universitys = get_all_universitys()
    '''
    subjects = get_all_subject()

    #pagenation

    paginator = Paginator(subjects, 20)
    page = request.GET.get('page')

    try:
        subjects = paginator.page(page)
    except PageNotAnInteger:
        #페이지가 숫자가 아니면 1번 페이지로
        subjects = paginator.page(1)
    except EmptyPage:
        #페이지 범위 초과시 마지막 페이지
        subjects = paginator.page(paginator.num_pages)
    context['subjects'] = subjects
    '''
    context['universitys'] = universitys
    return render(request, 'subject-manage.html', context)


# 일반 설정 생성 화면
def general_create(request):
    context = get_context_data(request, 'ruleActive')
    return render(request, 'general-create.html', context)

def general_update(request, id):
    context = get_context_data(request, 'ruleActive')
    context['meta_data'] = MetaDatainfo.objects.get(pk=id)
    return render(request, 'general-update.html', context)


# 일반 설정 화면 (메타데이터)
class general(ListView):
    model = MetaDatainfo
    template_name = 'general-setting.html'
    context_object_name = 'context'
    paginate_by = 30

    # search 용
    def get_queryset(self):
        try:
            meta_data_code = self.request.GET['meta_data_code']
            meta_data_name = self.request.GET['meta_data_name']
            meta_data_relation_code = self.request.GET['meta_data_relation_code']
            meta_data_relation_name = self.request.GET['meta_data_relation_name']
            meta_upper_data_code = self.request.GET['meta_upper_data_code']
        except:
            meta_data_code = ''
            meta_data_name = ''
            meta_data_relation_code = ''
            meta_data_relation_name = ''
            meta_upper_data_code = ''
        return MetaDatainfo.objects.filter(meta_data_code__icontains=meta_data_code,
                                           meta_data_name__icontains=meta_data_name,
                                           meta_data_relation_code__icontains=meta_data_relation_code,
                                           meta_data_relation_name__icontains=meta_data_relation_name,
                                           upper_data_code__icontains=meta_upper_data_code)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta_data_code'] = MetaDatainfo.objects.all().values('meta_data_code').distinct()
        context['meta_data_name'] = MetaDatainfo.objects.all().values('meta_data_name').distinct()
        context['meta_data_relation_code'] = MetaDatainfo.objects.all().values('meta_data_relation_code').distinct()
        context['meta_data_relation_name'] = MetaDatainfo.objects.all().values('meta_data_relation_name').distinct()
        context['upper_data_code'] = MetaDatainfo.objects.all().values('upper_data_code').distinct()
        return context

# 최초 로그인 화면
@login_required
def join(request):

    if request.method == 'GET':
        #StudentInfo가 없을시 최초 로그인
        #if request.user.is_staff is True:
        #    return redirect(reverse('index'))
        try:
            student_info = StudentInfo.objects.get(user_id=request.user.id)
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