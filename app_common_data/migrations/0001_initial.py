# Generated by Django 2.1.7 on 2019-06-20 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=20)),
                ('college_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CompletionDivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=20)),
                ('completion_division_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=20)),
                ('college_name', models.CharField(blank=True, max_length=20)),
                ('department_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MetaDatainfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_data_code', models.CharField(max_length=20)),
                ('meta_data_name', models.CharField(max_length=20)),
                ('meta_data_relation_code', models.CharField(max_length=20)),
                ('subdata_presence_yn', models.CharField(max_length=20)),
                ('meta_data_creation_date', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=20)),
                ('domain_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=20)),
                ('subject_code', models.CharField(max_length=20)),
                ('subject_name', models.CharField(max_length=20)),
                ('subject_completion_division', models.CharField(max_length=20)),
                ('subject_area', models.CharField(blank=True, max_length=20)),
                ('subject_credit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UniversityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=20)),
                ('university_max_grade', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='subjectinfo',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_common_data.UniversityInfo'),
        ),
        migrations.AddField(
            model_name='subjectdomain',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_common_data.UniversityInfo'),
        ),
        migrations.AddField(
            model_name='departmentinfo',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_common_data.UniversityInfo'),
        ),
        migrations.AddField(
            model_name='completiondivision',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_common_data.UniversityInfo'),
        ),
    ]
