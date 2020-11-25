# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-01 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradepath', '0016_auto_20180301_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='condition',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trade',
            name='fee_factor',
            field=models.CharField(blank=True, choices=[('ACTUAL', 'Actual'), ('PERCENT', 'Percent')], default=100, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='price_factor',
            field=models.CharField(choices=[('ACTUAL', 'Actual'), ('PERCENT', 'Percent')], default=100, max_length=15),
        ),
        migrations.AlterField(
            model_name='trade',
            name='venue',
            field=models.CharField(choices=[('CLEARPAR', 'ClearPar'), ('DIRECT', 'Direct Settlement'), ('OFFLINE', 'Offline'), ('OTHER', 'Other')], default='CLEARPAR', max_length=15),
        ),
    ]
