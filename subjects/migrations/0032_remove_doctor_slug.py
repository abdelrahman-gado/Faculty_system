# Generated by Django 3.2.9 on 2021-11-26 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0031_doctor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='slug',
        ),
    ]
