# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20170323_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='u_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='u_id',
        ),
        migrations.AlterField(
            model_name='acadamic_record',
            name='a_id',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AlterField(
            model_name='acadamic_record',
            name='quiz_marks',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='acadamic_record',
            name='quiz_number',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='group',
            name='files',
            field=models.FileField(max_length=500, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='group',
            name='g_id',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='cell_number',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_id',
            field=models.CharField(default='0', max_length=40),
        ),
    ]