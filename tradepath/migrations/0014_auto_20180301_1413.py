# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-01 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradepath', '0013_auto_20170917_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='investment_type',
            field=models.CharField(choices=[('BANK_LOAN', 'Bank Loan'), ('BOND', 'Bond'), ('EQUITY', 'Equity'), ('OTHER', 'Other')], default='OTHER', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='base',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='external_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='issuer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='spread',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='path',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('IN PROGRESS', 'In Progress'), ('NOT CIRCULATED', 'Not Circulated'), ('N/A', 'N/A'), ('COMPLETED', 'Completed')], default='PENDING', max_length=50),
        ),
    ]