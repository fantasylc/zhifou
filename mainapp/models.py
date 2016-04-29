#encoding:utf-8

# Create your models here.


from django.db import models
#from userauth.models import User
from django.conf import settings

class Topic(models.Model):
    title = models.CharField(max_length='20',verbose_name='标题')
    user_add = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='topics')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    summary = models.TextField(verbose_name='描述')
    parent = models.ForeignKey('self',default=None,blank=True,null=True,related_name='child', verbose_name='父话题')
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followtopics')

    class Meta:
        verbose_name_plural = verbose_name = '用户'

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=150,verbose_name='问题标题')
    intro = models.TextField(verbose_name='问题描述')
    time_add = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    time_update = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    views = models.IntegerField(default=0, verbose_name='浏览次数')
    topic = models.ForeignKey(Topic,default=None, verbose_name='话题')
    creater = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questions', verbose_name='提问者')
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='follques', verbose_name='关注者')

    class Meta:
        verbose_name=verbose_name_plural = '问题'

    def __str__(self):
        return self.title



class Answer(models.Model):
    content = models.TextField(verbose_name='回复')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='创建回复时间')
    time_update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    answerer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='回复者')
    question = models.ForeignKey(Question,related_name='answers', verbose_name='所属问题')
    colecter = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='colectanswers', verbose_name='收藏者')
    zantong = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='zantongs',  verbose_name='赞同者')

    class Meta:
        verbose_name = '回复'

    def __str__(self):
        return self.content[:30]




