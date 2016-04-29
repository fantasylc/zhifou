# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=30, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('name', models.CharField(verbose_name='昵称', default='改个昵称吧', max_length=30)),
                ('avatar', models.ImageField(verbose_name='头像', upload_to='avatars')),
                ('sex', models.CharField(verbose_name='性别', choices=[('man', '男'), ('women', '女')], default='man', max_length=10)),
                ('jianjie', models.CharField(verbose_name='简介', default='', max_length=100)),
                ('motto', models.CharField(verbose_name='座右铭', default='', max_length=100)),
                ('profession', models.CharField(verbose_name='行业', default='', max_length=30)),
                ('city', models.CharField(verbose_name='城市', default='', max_length=20)),
                ('school', models.CharField(verbose_name='毕业学校', default='', max_length=20)),
                ('educert', models.CharField(verbose_name='学历', default='', max_length=10)),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('follower', models.ManyToManyField(verbose_name='关注者', related_name='followed', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(to='auth.Group', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', related_query_name='user', blank=True)),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', related_name='user_set', help_text='Specific permissions for this user.', verbose_name='user permissions', related_query_name='user', blank=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-addtime'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
