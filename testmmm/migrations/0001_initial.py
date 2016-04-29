# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('stuff', models.ManyToManyField(blank=True, null=True, related_name='stuffre', to='testmmm.MyModel', verbose_name='description')),
            ],
        ),
    ]
