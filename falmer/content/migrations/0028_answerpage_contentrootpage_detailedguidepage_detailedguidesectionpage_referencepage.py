# Generated by Django 2.0.5 on 2018-07-02 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('content', '0027_freshershomepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Answer',
            },
            bases=('content.page',),
        ),
        migrations.CreateModel(
            name='ContentRootPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Content Root',
            },
            bases=('content.page',),
        ),
        migrations.CreateModel(
            name='DetailedGuidePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Detailed Guide',
            },
            bases=('content.page',),
        ),
        migrations.CreateModel(
            name='DetailedGuideSectionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Detailed Guide Section',
            },
            bases=('content.page',),
        ),
        migrations.CreateModel(
            name='ReferencePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Reference',
            },
            bases=('content.page',),
        ),
    ]