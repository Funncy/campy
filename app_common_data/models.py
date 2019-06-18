from django.db import models
    
# 메타데이터정보
class MetaDatainfo(models.Model):

    # 메타 데이터 코드
    # 메타 데이터 이름
    # 메타 관련 데이터 코드
    # 메타 관련 데이터 이름
    # 하위 데이터 존재 여부
    # 메타 데이터 생성 일자

    meta_data_code = models.CharField(max_length=20)
    meta_data_name = models.CharField(max_length=20)
    meta_data_relation_code = models.CharField(max_length=20)
    meta_data_relation_code = models.CharField(max_length=20)
    subdata_presence_yn = models.CharField(max_length=20)
    meta_data_creation_date= models.CharField(max_length=20)
