# Generated by Django 2.1.5 on 2019-04-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_data_conversion', '0002_auto_20190430_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('가', models.CharField(max_length=50)),
                ('나', models.CharField(max_length=50)),
                ('다', models.CharField(max_length=50)),
            ],
        ),
    ]
