# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-09-13 15:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0011_auto_20160913_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='requires_environmentalchecks',
            new_name='requires_environmental_checks',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='requires_plannedmaintenance',
            new_name='requires_planned_maintenance',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='requires_safetychecks',
            new_name='requires_safety_checks',
        ),
    ]