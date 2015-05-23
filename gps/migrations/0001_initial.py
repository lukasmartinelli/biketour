# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('accuracy', models.FloatField()),
                ('speed', models.FloatField()),
                ('battery', models.FloatField()),
                ('satellites', models.FloatField()),
                ('direction', models.FloatField()),
                ('provider', models.CharField(max_length=50)),
                ('native_altitude', models.FloatField()),
                ('google_altitude', models.FloatField()),
            ],
        ),
    ]
