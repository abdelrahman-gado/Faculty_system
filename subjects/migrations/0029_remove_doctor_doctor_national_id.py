# Generated by Django 3.2.9 on 2021-11-23 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0028_auto_20211123_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_national_id',
        ),
    ]
