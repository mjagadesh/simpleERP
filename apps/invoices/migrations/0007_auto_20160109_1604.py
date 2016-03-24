# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0006_auto_20160109_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name': 'Invoice', 'verbose_name_plural': 'Invoices'},
        ),
        migrations.AlterModelOptions(
            name='invoiceposition',
            options={'verbose_name': 'Invoice position', 'verbose_name_plural': 'Invoice positions'},
        ),
        migrations.AlterModelOptions(
            name='invoiceseries',
            options={'verbose_name': 'Invoice series', 'verbose_name_plural': 'Invoice series'},
        ),
        migrations.AddField(
            model_name='invoice',
            name='money_gross',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=32, verbose_name='Price gross'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='money_net',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=32, verbose_name='Price net'),
        ),
        migrations.AlterField(
            model_name='invoiceposition',
            name='tax',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, verbose_name='Tax'),
        ),
    ]