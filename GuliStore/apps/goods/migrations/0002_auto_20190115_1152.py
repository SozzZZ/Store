# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-15 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='goods_sn',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='商品编号'),
        ),
    ]