# Generated by Django 2.0.8 on 2018-08-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matte', '0009_auto_20180406_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='matteimage',
            name='file_hash',
            field=models.CharField(blank=True, editable=False, max_length=40),
        ),
    ]
