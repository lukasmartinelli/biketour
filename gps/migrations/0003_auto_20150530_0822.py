# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0002_auto_20150529_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='accuracy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='battery',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='direction',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='google_altitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='native_altitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='provider',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='point',
            name='satellites',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='speed',
            field=models.FloatField(null=True),
        ),
    ]
