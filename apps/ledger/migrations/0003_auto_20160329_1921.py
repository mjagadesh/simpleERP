# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-29 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_ledgerentry_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledgerentry',
            name='column_15',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Additional info (not required)'),
        ),
        migrations.AlterField(
            model_name='ledgerentry',
            name='comments',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Comments'),
        ),
    ]
