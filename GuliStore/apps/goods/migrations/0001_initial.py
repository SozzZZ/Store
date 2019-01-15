# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-14 21:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='goods/image', verbose_name='首页轮播图')),
                ('index', models.IntegerField(verbose_name='轮播顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '首页轮播图信息',
                'verbose_name_plural': '首页轮播图信息',
            },
        ),
        migrations.CreateModel(
            name='CategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='brand/images', verbose_name='赞助图片')),
                ('name', models.CharField(max_length=20, verbose_name='赞助名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '赞助信息',
                'verbose_name_plural': '赞助信息',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='商品类别名称')),
                ('category_type', models.IntegerField(choices=[(1, '一级'), (2, '二级'), (3, '三级')], verbose_name='类别级别')),
                ('code', models.CharField(max_length=50, verbose_name='类别编号')),
                ('is_tab', models.BooleanField(default=False, verbose_name='是否导航')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='所属类别')),
            ],
            options={
                'verbose_name': '商品类别信息',
                'verbose_name_plural': '商品类别信息',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='goods/image', verbose_name='商品轮播图')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品轮播图信息',
                'verbose_name_plural': '商品轮播图信息',
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='商品名称')),
                ('goods_sn', models.CharField(max_length=30, verbose_name='商品编号')),
                ('goods_brief', models.CharField(blank=True, max_length=300, null=True, verbose_name='商品简介')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='商品详情')),
                ('goods_front_image', models.ImageField(max_length=200, upload_to='goods/images', verbose_name='商品封面')),
                ('market_price', models.FloatField(verbose_name='商品市场价')),
                ('shop_price', models.FloatField(verbose_name='商品店铺价')),
                ('ship_free', models.BooleanField(default=True, verbose_name='是否包邮')),
                ('click_num', models.IntegerField(default=0, verbose_name='商品浏览数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='商品收藏数')),
                ('goods_num', models.IntegerField(default=100, verbose_name='商品库存数量')),
                ('sold_num', models.IntegerField(default=0, verbose_name='商品销量')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热卖')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否为新')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.GoodsCategory', verbose_name='所属类别')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
            },
        ),
        migrations.AddField(
            model_name='goodsimage',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='goods.GoodsInfo', verbose_name='所属商品'),
        ),
        migrations.AddField(
            model_name='categorybrand',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.GoodsCategory', verbose_name='所属类别'),
        ),
        migrations.AddField(
            model_name='banner',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banners', to='goods.GoodsInfo', verbose_name='所属商品'),
        ),
    ]
