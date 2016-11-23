# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch_out', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime', models.CharField(max_length=45)),
                ('date', models.DateTimeField()),
                ('address', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.AddField(
            model_name='alerts',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch_out.User'),
        ),
    ]
