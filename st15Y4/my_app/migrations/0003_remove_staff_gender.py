# Generated by Django 5.2.3 on 2025-06-24 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='gender',
        ),
    ]
