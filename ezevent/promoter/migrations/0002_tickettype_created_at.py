# Generated by Django 5.1.4 on 2025-02-24 22:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promoter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
