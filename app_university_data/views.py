from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SubjectSerializer
from .models import SubjectInfo
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SubjectsViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SubjectInfo.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        university = self.request.query_params.get('university')
        return SubjectInfo.objects.filter(university_name=university)


class SubjectViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SubjectInfo.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        university = self.request.query_params.get('university')
        subject = self.request.query_params.get('subject')
        return SubjectInfo.objects.filter(university_name=university, subject_name=subject)
