# Generated by Django 2.1.5 on 2019-06-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=20)),
                ('student_admission_year', models.CharField(max_length=20)),
                ('student_major_division', models.CharField(max_length=20)),
                ('student_major_name', models.CharField(max_length=20)),
                ('student_university_name', models.CharField(max_length=20)),
                ('student_college_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=20)),
                ('user_contact_number', models.CharField(max_length=20, null=True)),
                ('user_privilege', models.CharField(max_length=20, null=True)),
                ('user_university_name', models.CharField(max_length=20)),
            ],
        ),
    ]
