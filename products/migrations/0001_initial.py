# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-28 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='post date')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
