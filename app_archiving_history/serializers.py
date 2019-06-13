from rest_framework import serializers
from .models import archieving_history
from app_common_data.serializers import SubjectSerializer

class HistorySerializer(serializers.ModelSerializer):
    history_subject_code = SubjectSerializer
    class Meta:
        model = archieving_history
        fields = ('__all__')