# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='回复')),
                ('time_add', models.DateTimeField(verbose_name='创建回复时间', auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('answerer', models.ForeignKey(verbose_name='回复者', to=settings.AUTH_USER_MODEL)),
                ('colecter', models.ManyToManyField(related_name='colectanswers', verbose_name='收藏者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '回复',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='问题标题', max_length=150)),
                ('intro', models.TextField(verbose_name='问题描述')),
                ('time_add', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('views', models.IntegerField(default=0, verbose_name='浏览次数')),
                ('creater', models.ForeignKey(related_name='questions', verbose_name='提问者', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ManyToManyField(related_name='follques', verbose_name='关注者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '问题',
                'verbose_name_plural': '问题',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='标题', max_length='20')),
                ('time_add', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('summary', models.TextField(verbose_name='描述')),
                ('follower', models.ManyToManyField(related_name='followtopics', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(default=None, to='mainapp.Topic', blank=True, verbose_name='父话题', related_name='child', null=True)),
                ('user_add', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='topics')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(default=None, verbose_name='话题', to='mainapp.Topic'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers', verbose_name='所属问题', to='mainapp.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='zantong',
            field=models.ManyToManyField(related_name='zantongs', verbose_name='赞同者', to=settings.AUTH_USER_MODEL),
        ),
    ]
