from rest_framework import serializers
from .models import MetaDatainfo

class MetaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaDatainfo
        fields = ('__all__')