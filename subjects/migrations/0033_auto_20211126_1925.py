# Generated by Django 3.2.9 on 2021-11-26 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0032_remove_doctor_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.AddField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
