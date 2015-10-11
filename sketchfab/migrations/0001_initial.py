# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date_obtained', models.DateField(default=django.utils.timezone.now)),
                ('badge', models.ForeignKey(to='sketchfab.Badge')),
            ],
        ),
        migrations.CreateModel(
            name='Model3D',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(unique=True, max_length=200)),
                ('email', models.CharField(unique=True, max_length=200)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('badges', models.ManyToManyField(to='sketchfab.Badge', through='sketchfab.Milestone')),
            ],
        ),
        migrations.AddField(
            model_name='model3d',
            name='user',
            field=models.ForeignKey(to='sketchfab.User'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='user',
            field=models.ForeignKey(to='sketchfab.User'),
        ),
    ]
