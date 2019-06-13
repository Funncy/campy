from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HistorySerializer
from .models import archieving_history

# Create your views here.

#화면 렌더링
def history(request):
    return render(request, 'history.html', {})

class HistoryViewset(viewsets.ModelViewSet):
    queryset = archieving_history.objects.all()
    serializer_class = HistorySerializer
