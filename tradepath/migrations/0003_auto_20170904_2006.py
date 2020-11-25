# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradepath', '0002_auto_20170904_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='action',
            field=models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell')], default='buy', max_length=10),
        ),
        migrations.AlterField(
            model_name='trade',
            name='market',
            field=models.CharField(choices=[('PRIMARY', 'Primary'), ('SECONDARY', 'Secondary')], default='primary', max_length=10),
        ),
        migrations.AlterField(
            model_name='trade',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('ACTIVE', 'Active'), ('CLOSED', 'Closed'), ('CANCELLED', 'Cancelled')], default='draft', max_length=10),
        ),
    ]