# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-17 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0038_qrlocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='grn',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
