from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HistorySerializer
from .models import archieving_history
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

#화면 렌더링
@login_required
def history(request):
    return render(request, 'history.html', {})

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
        #외부 데이터 post 데이터에 연결 하기
        #copy로 데이터 복사해와서 처리
        post_user = request.data.copy()
        # self에는 ajax로 보낸 request post data가 안담김... 일반 request에 담겨있
        # post_user = self.request.POST.dict().copy()
        # post_user.update({"history_user_id": request.user.id})
        post_user.update({"history_user_id": request.user.id})
        #수정한 post데이터 넣기 request 말고
        serializer = self.get_serializer(data=post_user)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
