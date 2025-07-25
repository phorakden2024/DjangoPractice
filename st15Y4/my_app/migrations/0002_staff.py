# Generated by Django 5.2.3 on 2025-06-24 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.BooleanField(default=True)),
                ('dateofbirth', models.DateField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.position')),
            ],
        ),
    ]
