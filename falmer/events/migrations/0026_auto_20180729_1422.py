# Generated by Django 2.0.7 on 2018-07-29 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_auto_20180628_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mslevent',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='mslevent', serialize=False, to='events.Event'),
        ),
    ]
