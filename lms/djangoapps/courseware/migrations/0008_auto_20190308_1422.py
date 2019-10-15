# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-08 22:22
from __future__ import unicode_literals

from django.db import migrations
import opaque_keys.edx.django.models


class Migration(migrations.Migration):

    dependencies = [
        ('courseware', '0007_remove_done_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepreference',
            name='course_id',
            field=opaque_keys.edx.django.models.CourseKeyField(db_index=True, max_length=255),
        ),
    ]
