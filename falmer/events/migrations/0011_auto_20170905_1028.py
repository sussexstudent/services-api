# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20170821_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mslevent',
            name='title',
            field=models.TextField(),
        ),
    ]
