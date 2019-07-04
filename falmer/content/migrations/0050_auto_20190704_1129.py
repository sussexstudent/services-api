# Generated by Django 2.2.3 on 2019-07-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0049_auto_20190702_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeroverviewpage',
            name='facebook_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='officeroverviewpage',
            name='instagram_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='officeroverviewpage',
            name='twitter_username',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='officeroverviewpage',
            name='youtube_splash',
            field=models.URLField(blank=True, default=''),
        ),
    ]