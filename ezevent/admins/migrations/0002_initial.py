# Generated by Django 5.1.4 on 2025-02-23 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admins', '0001_initial'),
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signuptoken',
            name='role',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='auths.role'),
        ),
    ]
