from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HistorySerializer
from .models import archieving_history
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from app_common_data.models import SubjectInfo
from django.shortcuts import get_object_or_404

# Create your views here.

class HistoryViewset(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)

    queryset = archieving_history.objects.all()
    serializer_class = HistorySerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return archieving_history.objects.filter(history_user_id=user_id)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        # request 데이터 dict 복사
        data = request.data.dict().copy()

        # subject_name 으로 subject 정보 가져오기
        subject = SubjectInfo.objects.get(university_name=data['university'], subject_name=data['history_subject_name'])
        # data에 과목데이터 추가
        data['history_subject_code'] = subject.__dict__['id']
        data['history_subject_area'] = subject.__dict__['subject_area'] + '영역'
        data['history_subject_credit'] = subject.__dict__['subject_credit']
        data['history_subject_assessment_Methods'] = 'test'

        print(data)
        # 수정된 데이터 삽입
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            #추가적인 외래키 요소들 연결하기 (id값으로)
            serializer.save(history_user_id = request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
