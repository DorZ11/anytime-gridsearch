# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-14 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grids', '0005_rename_dataset_columns'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvresult',
            name='errors',
            field=models.TextField(blank=True, null=True),
        ),
    ]
