# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-17 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0040_auto_20171017_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='dispatch_note',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
