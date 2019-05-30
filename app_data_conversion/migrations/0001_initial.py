# Generated by Django 2.1.5 on 2019-05-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataDumpo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NO', models.CharField(max_length=50)),
                ('년도', models.CharField(max_length=50)),
                ('학기', models.CharField(max_length=50)),
                ('개설대학', models.CharField(max_length=50)),
                ('개설학과전공', models.CharField(max_length=50)),
                ('학수번호', models.CharField(max_length=50)),
                ('분반', models.CharField(max_length=50)),
                ('교과목명', models.CharField(max_length=50)),
                ('이수구분', models.CharField(max_length=50)),
                ('선택영역', models.CharField(max_length=50)),
                ('학년', models.CharField(max_length=50)),
                ('학점', models.CharField(max_length=50)),
                ('이론', models.CharField(max_length=50)),
                ('실습', models.CharField(max_length=50)),
                ('수강인원', models.CharField(max_length=50)),
                ('요일및강의시간', models.CharField(max_length=50)),
                ('강의실', models.CharField(max_length=50)),
                ('교수명', models.CharField(max_length=50)),
                ('수강대상및유의사항', models.CharField(max_length=50)),
                ('사이버강좌', models.CharField(max_length=50)),
                ('강의언어', models.CharField(max_length=50)),
                ('수업유형', models.CharField(max_length=50)),
                ('수강제한', models.CharField(max_length=50)),
                ('강의평가유형', models.CharField(max_length=50)),
                ('강사료', models.CharField(max_length=50)),
                ('메인교수소속', models.CharField(max_length=50)),
                ('이번교수명', models.CharField(max_length=50)),
                ('이번교수소속', models.CharField(max_length=50)),
                ('삼번교수명', models.CharField(max_length=50)),
                ('삼번교수소속', models.CharField(max_length=50)),
                ('주관학과', models.CharField(max_length=50)),
                ('강의실수용인원', models.CharField(max_length=50)),
                ('관심과목등록수', models.CharField(max_length=50)),
                ('외국인전용', models.CharField(max_length=50)),
                ('내국인전용', models.CharField(max_length=50)),
            ],
        ),
    ]
