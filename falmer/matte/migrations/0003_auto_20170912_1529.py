# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matte', '0002_remoteimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matteimage',
            options={'permissions': (('can_list_all', 'Can list all images'),)},
        ),
    ]
