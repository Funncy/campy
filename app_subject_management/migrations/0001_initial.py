from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=20)),
                ('subject_name', models.CharField(max_length=20)),
                ('subject_division', models.CharField(max_length=20)),
                ('subject_area', models.CharField(max_length=20)),
                ('subject_credit', models.CharField(max_length=20)),
                ('subject_assessment_Methods', models.CharField(max_length=20)),
            ],
        ),
    ]
