# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-04 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('honghua', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='cardno',
        ),
    ]