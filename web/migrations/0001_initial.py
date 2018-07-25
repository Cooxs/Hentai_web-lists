# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-14 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标题')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '大分类',
                'verbose_name_plural': '大分类',
                'ordering': ['created_time'],
            },
        ),
        migrations.CreateModel(
            name='Guonei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标题')),
                ('desc', models.CharField(blank=True, max_length=100, verbose_name='描述')),
                ('image_url', models.ImageField(upload_to='images/guonei/%Y/%m/%d', verbose_name='图片')),
                ('true_url', models.URLField(blank=True, max_length=100, verbose_name='地址')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '国内站点',
                'verbose_name_plural': '国内站点',
                'ordering': ['created_time'],
            },
        ),
        migrations.CreateModel(
            name='Haiwai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标题')),
                ('desc', models.CharField(blank=True, max_length=100, verbose_name='描述')),
                ('image_url', models.ImageField(upload_to='images/haiwai/%Y/%m/%d', verbose_name='图片')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '海外站点',
                'verbose_name_plural': '海外站点',
                'ordering': ['created_time'],
            },
        ),
        migrations.CreateModel(
            name='SmallCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标题')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Category', verbose_name='站点分类')),
            ],
            options={
                'verbose_name': '小分类',
                'verbose_name_plural': '小分类',
                'ordering': ['created_time'],
            },
        ),
        migrations.AddField(
            model_name='haiwai',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.SmallCategory', verbose_name='站点分类'),
        ),
        migrations.AddField(
            model_name='guonei',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.SmallCategory', verbose_name='站点分类'),
        ),
    ]
