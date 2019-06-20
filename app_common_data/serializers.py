from rest_framework import serializers
from .models import UniversityInfo, DepartmentInfo, CompletionDivision

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityInfo
        fields = ('__all__')

class DepartmentSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    class Meta:
        model = DepartmentInfo
        fields = ('__all__')

class CompletionDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletionDivision
        fields = ('__all__')