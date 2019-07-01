from rest_framework import serializers
from .models import archieving_history, graduation_rule, graduation_subject_group, graduation_subject_group_mapping

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = archieving_history
        fields = ('__all__')

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = graduation_rule
        fields = ('__all__')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = graduation_subject_group
        fields = ('__all__')

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = graduation_subject_group_mapping
        fields = ('__all__')

class GroupAndMappingSerializer(serializers.ModelSerializer):
    mappings = MappingSerializer(many=True)
    class Meta:
        model =graduation_subject_group
        fields = ('subject_group_name', 'subject_group_university_name', 'mappings')