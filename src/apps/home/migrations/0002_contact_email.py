# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Correo'),
        ),
    ]
