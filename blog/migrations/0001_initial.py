# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tag', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('summary', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
