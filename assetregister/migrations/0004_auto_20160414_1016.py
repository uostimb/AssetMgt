# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-14 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0003_auto_20160414_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='acquired_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
