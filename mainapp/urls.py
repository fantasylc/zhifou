__author__ = 'liuchao'
from django.conf.urls import url,patterns

urlpatterns = patterns('mainapp.views',
                       url(r'','index',name='index'),
                       
                       )