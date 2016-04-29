# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_auto_20160421_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='active_code',
            field=models.CharField(max_length=200, default='', verbose_name='激活码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=10, default='man', choices=[('women', '女'), ('man', '男')], verbose_name='性别'),
        ),
    ]
