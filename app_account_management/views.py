from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import StudentInfo
from allauth.socialaccount.models import SocialAccount

# Create your views here.

@login_required
def join(request):

    if request.method == 'GET':
        #StudentInfo가 없을시 최초 로그인
        try:
            student_info = StudentInfo.objects.get(user_id=request.user.id)
        except StudentInfo.DoesNotExist:
            return render(request, 'join.html', {})

        #Studentinfo가 있을경우 메인화면으로 이동
        return redirect(reverse('index'))
    return