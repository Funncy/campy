from rest_framework import serializers
from .models import archieving_history

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = archieving_history
        fields = ('__all__')