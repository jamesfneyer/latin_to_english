# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latin', models.CharField(max_length=200)),
                ('conjugation', models.CharField(max_length=200)),
                ('parts_of_speech', models.CharField(max_length=13)),
                ('definition', models.TextField()),
                ('english', models.CharField(max_length=200)),
            ],
        ),
    ]
