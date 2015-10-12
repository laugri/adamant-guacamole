# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sketchfab', '0002_auto_20151011_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='model3d',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
