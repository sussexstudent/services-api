# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import falmer.content.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('matte', '0008_matteimage_internal_source'),
        ('content', '0020_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='OffersPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.page',),
        ),
        migrations.CreateModel(
            name='SingleOfferPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('company_name', models.CharField(max_length=255)),
                ('deal_tag', models.CharField(max_length=255)),
                ('company_website', models.URLField(blank=True, default='')),
                ('main', wagtail.core.fields.StreamField((('text', wagtail.core.blocks.StructBlock((('value', wagtail.core.blocks.RichTextBlock()),))), ('image', wagtail.core.blocks.StructBlock((('image', falmer.content.blocks.FalmerImageChooserBlock(required=True)), ('alternative_title', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))))), ('callout', wagtail.core.blocks.StructBlock((('value', wagtail.core.blocks.StructBlock((('value', wagtail.core.blocks.RichTextBlock()),))), ('variant', wagtail.core.blocks.ChoiceBlock(choices=[('info', 'Info'), ('warning', 'Warning'), ('alert', 'Alert')], label='Variant')))))))),
                ('company_logo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matte.MatteImage')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.page',),
        ),
    ]
