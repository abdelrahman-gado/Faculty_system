# Generated by Django 3.2.9 on 2021-11-12 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bra', to='subjects.branch'),
        ),
    ]
