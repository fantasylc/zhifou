# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_auto_20160421_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(verbose_name='是否激活', default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(verbose_name='性别', max_length=10, choices=[('women', '女'), ('man', '男')], default='man'),
        ),
    ]
