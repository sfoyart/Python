# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/all-images', verbose_name='Picture'),
        ),
    ]
