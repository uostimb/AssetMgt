# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-15 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0007_asset_related_to_other_asset'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='asset_manufacturer',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]