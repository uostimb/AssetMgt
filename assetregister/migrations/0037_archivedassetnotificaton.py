# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-10 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0036_amrcgroup_ad_ou_group_mapping'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedAssetNotificaton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
    ]