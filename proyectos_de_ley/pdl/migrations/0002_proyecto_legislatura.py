# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-02 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='legislatura',
            field=models.IntegerField(default=2011, max_length=4),
            preserve_default=False,
        ),
    ]
