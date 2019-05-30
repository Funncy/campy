from rest_framework import serializers
from .models import UniversityInfo

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityInfo
        fields = ('__all__')