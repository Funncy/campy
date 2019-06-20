from django.db import models

# Create your models here.

# 메타데이터정보
class MetaDatainfo(models.Model):
    # 메타 데이터 코드
    # 메타 데이터 이름
    # 메타 관련 데이터 코드
    # 메타 관련 데이터 이름
    # 상위 데이터 코드
    # 메타 데이터 생성 일자

    meta_data_code = models.CharField(max_length=50)
    meta_data_name = models.CharField(max_length=50)
    meta_data_relation_code = models.CharField(max_length=50)
    meta_data_relation_name = models.CharField(max_length=50)
    upper_data_code = models.CharField(max_length=50, blank=True)
    # meta_data_creation_date = models.DateTimeField(auto_now_add=True)

