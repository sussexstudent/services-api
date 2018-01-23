# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-23 13:56
from __future__ import unicode_literals

from django.db import migrations
import falmer.content.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0004_referencepage_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencepage',
            name='main',
            field=wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.StructBlock((('value', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('callout', wagtail.wagtailcore.blocks.StructBlock((('value', wagtail.wagtailcore.blocks.StructBlock((('value', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('variant', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('info', 'Info'), ('warning', 'Warning'), ('alert', 'Alert')], label='Variant'))))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', falmer.content.blocks.FalmerImageChooserBlock(required=True)), ('alternative_title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('caption', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('button_group_links', wagtail.wagtailcore.blocks.StreamBlock((('internal_link', wagtail.wagtailcore.blocks.StructBlock((('link', falmer.content.blocks.FalmerPageChooserBlock(required=True)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False))), label='Internal page')), ('external_link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=True)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('target', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('', 'Open link in'), ('_self', 'Same window'), ('_blank', 'New window')], help_text='Open link in'))), label='External Page')))))), blank=True, null=True, verbose_name='Main Content'),
        ),
    ]
