# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0009_auto_20160422_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(default='man', choices=[('man', '男'), ('women', '女')], verbose_name='性别', max_length=10),
        ),
    ]
