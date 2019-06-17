from rest_framework import serializers
from .models import archieving_history
from app_common_data.serializers import SubjectSerializer
from rest_framework.serializers import PrimaryKeyRelatedField

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = archieving_history
        fields = ('__all__')