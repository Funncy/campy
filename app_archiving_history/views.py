from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HistorySerializer
from .models import archieving_history
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated

# Create your views here.

#화면 렌더링
@login_required
def history(request):
    return render(request, 'history.html', {})

class HistoryViewset(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)

    queryset = archieving_history.objects.all()
    serializer_class = HistorySerializer
