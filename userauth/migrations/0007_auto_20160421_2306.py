# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0006_auto_20160421_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(verbose_name='性别', default='man', choices=[('man', '男'), ('women', '女')], max_length=10),
        ),
    ]
