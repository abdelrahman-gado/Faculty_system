# Generated by Django 3.2.9 on 2021-11-23 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0026_remove_doctor_doctor_national_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='doctor_national_id',
            field=models.CharField(default='', max_length=14),
            preserve_default=False,
        ),
    ]
