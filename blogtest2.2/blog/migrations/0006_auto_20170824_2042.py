# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-24 12:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='catagory_id',
            new_name='catagory',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='tag_id',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='article_id',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='pid_id',
            new_name='pid',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
    ]
