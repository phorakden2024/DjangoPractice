# Generated by Django 5.2.3 on 2025-07-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_alter_teacher_create_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='update_at',
            field=models.DateTimeField(),
        ),
    ]
