from rest_framework import serializers
from .models import MetaDatainfo

class MetaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaDatainfo
        fields = ('__all__')

class MetaCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaDatainfo
        fields = ('meta_data_code', 'meta_data_name')

class MetaRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaDatainfo
        fields = ('meta_data_relation_code', 'meta_data_relation_name')