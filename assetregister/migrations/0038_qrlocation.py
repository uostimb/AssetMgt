# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-13 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0037_archivedassetnotificaton'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRLocation',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_room', models.CharField(blank=True, max_length=255, null=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qr_building', to='assetregister.Buildings')),
            ],
        ),
    ]