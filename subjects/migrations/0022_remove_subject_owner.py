# Generated by Django 3.2.9 on 2021-11-23 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0021_subject_doctor_national_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='owner',
        ),
    ]
