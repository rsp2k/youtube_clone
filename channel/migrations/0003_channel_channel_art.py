# Generated by Django 3.2.7 on 2022-09-12 12:19

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_auto_20220907_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='channel_art',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path),
        ),
    ]