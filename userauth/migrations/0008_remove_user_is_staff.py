# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0007_auto_20160421_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
