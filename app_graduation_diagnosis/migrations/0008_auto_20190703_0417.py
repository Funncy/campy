# Generated by Django 2.1.7 on 2019-07-03 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_graduation_diagnosis', '0007_auto_20190701_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduation_rule',
            name='rule_subject_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_graduation_diagnosis.graduation_subject_group'),
        ),
    ]
