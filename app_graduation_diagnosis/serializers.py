from rest_framework import serializers
from .models import archieving_history, graduation_rule

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = archieving_history
        fields = ('__all__')

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = graduation_rule
        fields = ('__all__')