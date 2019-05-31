from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePlanning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('course_plan_code', models.CharField(max_length=20)),
                ('course_plan_name', models.CharField(max_length=20)),
                ('lecture_code', models.CharField(max_length=20)),
                ('lecture_alarm', models.CharField(max_length=20)),
                ('course_schedule_yn', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LectureCalendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_code', models.CharField(max_length=20)),
                ('lecture_subject_code', models.CharField(max_length=20)),
                ('lecture_subject_name', models.CharField(max_length=20)),
                ('lecture_teacher_name', models.CharField(max_length=20)),
                ('lecture_place', models.CharField(max_length=20)),
                ('lecture_week_expression', models.CharField(max_length=20)),
                ('lecture_date', models.CharField(max_length=20)),
                ('lecture_star_time', models.CharField(max_length=20)),
                ('lecture_end_time', models.CharField(max_length=20)),
                ('lecture_opened_year', models.CharField(max_length=20)),
                ('lecture_opened_semester', models.CharField(max_length=20)),
                ('lecture_opened_department', models.CharField(max_length=20)),
            ],
        ),
    ]
