# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-15 18:20
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20190115_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='博客内容'),
        ),
    ]
