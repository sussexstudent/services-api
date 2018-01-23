# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 13:06
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0003_auto_20180119_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencepage',
            name='main',
            field=wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.StructBlock((('value', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('alternative_title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('caption', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('button_group_links', wagtail.wagtailcore.blocks.StreamBlock((('internal_link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=True)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False))), label='Internal page')), ('external_link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=True)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('target', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('', 'Open link in'), ('_self', 'Same window'), ('_blank', 'New window')], help_text='Open link in'))), label='External Page')))))), blank=True, null=True, verbose_name='Main Content'),
        ),
    ]
