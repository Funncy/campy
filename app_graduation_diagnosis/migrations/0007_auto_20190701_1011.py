# Generated by Django 2.1.7 on 2019-07-01 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_graduation_diagnosis', '0006_graduation_subject_group_graduation_subject_group_mapping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduation_subject_group_mapping',
            name='mapping_subject_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mappings', to='app_graduation_diagnosis.graduation_subject_group'),
        ),
    ]
