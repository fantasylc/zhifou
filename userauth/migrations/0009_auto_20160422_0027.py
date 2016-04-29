# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0008_remove_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=10, default='man', verbose_name='性别', choices=[('women', '女'), ('man', '男')]),
        ),
    ]
