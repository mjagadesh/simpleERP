# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-08 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.PositiveIntegerField(choices=[(1, 'Private person'), (2, 'Company')], verbose_name='Type')),
            ],
        ),
    ]
