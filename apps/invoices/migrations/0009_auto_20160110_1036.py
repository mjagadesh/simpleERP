# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0008_invoiceposition_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoiceposition',
            name='money_gross',
        ),
        migrations.AddField(
            model_name='invoiceposition',
            name='count',
            field=models.IntegerField(default=1, verbose_name='Count'),
        ),
        migrations.AddField(
            model_name='invoiceposition',
            name='total_gross',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=32, verbose_name='Total gross'),
        ),
        migrations.AddField(
            model_name='invoiceposition',
            name='total_net',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=32, verbose_name='Total net'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='money_gross',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='The price will change automatically when you change an invoice position', max_digits=32, verbose_name='Price gross'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='money_net',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='The price will change automatically when you change an invoice position', max_digits=32, verbose_name='Price net'),
        ),
    ]
