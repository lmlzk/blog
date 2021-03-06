# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-24 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170823_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(upload_to='static/ad/%m', verbose_name='图片路径'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar/default.png', max_length=200, upload_to='static/avatar/%m', verbose_name='头像'),
        ),
    ]
