# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gondola', '0008_auto_20170225_1809'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gondola',
            options={'ordering': ['position'], 'verbose_name_plural': 'gondole'},
        ),
        migrations.AddField(
            model_name='gondola',
            name='position',
            field=models.SmallIntegerField(default=1),
        ),
    ]
