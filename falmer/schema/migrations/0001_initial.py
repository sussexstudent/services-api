# Generated by Django 2.2.2 on 2019-07-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersistedQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha256_hash', models.CharField(db_index=True, max_length=256, unique=True)),
                ('query', models.TextField(unique=True)),
            ],
        ),
    ]
