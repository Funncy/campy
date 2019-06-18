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
        #serializer 초기화
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            #추가적인 외래키 요소들 연결하기 (id값으로)
            serializer.save(history_subject_code_id = 1, history_user_id = request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
