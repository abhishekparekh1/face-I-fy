# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-27 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(default=b'default', max_length=10)),
                ('time_stamp', models.CharField(default=b'', max_length=100)),
                ('is_consumed', models.BooleanField(default=False)),
            ],
        ),
    ]