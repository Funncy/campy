# Generated by Django 2.1.7 on 2019-06-27 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_graduation_diagnosis', '0005_auto_20190625_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='graduation_subject_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_group_name', models.CharField(max_length=50)),
                ('subject_group_university_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='graduation_subject_group_mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapping_completion_division', models.CharField(blank=True, max_length=50)),
                ('mapping_area', models.CharField(blank=True, max_length=50)),
                ('mapping_subject_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_graduation_diagnosis.graduation_subject_group')),
            ],
        ),
    ]
