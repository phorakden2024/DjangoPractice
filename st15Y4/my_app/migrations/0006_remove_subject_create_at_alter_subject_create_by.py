# Generated by Django 5.2.3 on 2025-07-12 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_subject_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='create_at',
        ),
        migrations.AlterField(
            model_name='subject',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.staff'),
        ),
    ]
