# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 13:06
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0003_auto_20180119_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencepage',
            name='main',
            field=wagtail.core.fields.StreamField((('text', wagtail.core.blocks.StructBlock((('value', wagtail.core.blocks.RichTextBlock()),))), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alternative_title', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))))), ('button_group_links', wagtail.core.blocks.StreamBlock((('internal_link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.PageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(required=False))), label='Internal page')), ('external_link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.URLBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(required=True)), ('target', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Open link in'), ('_self', 'Same window'), ('_blank', 'New window')], help_text='Open link in'))), label='External Page')))))), blank=True, null=True, verbose_name='Main Content'),
        ),
    ]
