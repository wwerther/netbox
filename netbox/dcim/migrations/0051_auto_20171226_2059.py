# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0050_connectioninterface_add_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfaceconnection',
            name='connection_name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
