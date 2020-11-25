# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 23:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tradepath', '0008_auto_20170904_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocation',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('READY', 'Ready'), ('SETTLED', 'Settled'), ('HOLD', 'On Hold')], default='PENDING', max_length=10),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='trade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allocations', to='tradepath.Trade'),
        ),
    ]