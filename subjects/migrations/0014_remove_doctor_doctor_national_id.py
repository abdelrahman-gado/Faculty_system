# Generated by Django 3.2.9 on 2021-11-20 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0013_alter_doctor_doctor_national_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_national_id',
        ),
    ]