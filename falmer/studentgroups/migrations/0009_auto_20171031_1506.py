# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('studentgroups', '0008_auto_20171031_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='award',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True),
        ),
        migrations.AddField(
            model_name='awardauthority',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='groupawarded',
            unique_together=set([('group', 'award', 'year')]),
        ),
    ]
