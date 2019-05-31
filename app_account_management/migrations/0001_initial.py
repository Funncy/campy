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
                ('student_college_name', models.CharField(max_length=20)),
            ],
        ),
    ]
