from rest_framework import serializers
from .models import SubjectInfo

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectInfo
        fields = ('__all__')

