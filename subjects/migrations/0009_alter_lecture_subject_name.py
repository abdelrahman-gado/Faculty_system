# Generated by Django 3.2.9 on 2021-11-20 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0008_auto_20211120_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='subject_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='subjects.subject'),
        ),
    ]
