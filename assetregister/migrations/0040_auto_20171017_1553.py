# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-17 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0039_asset_grn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='grn',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
