__author__ = 'liuchao'
from django.conf.urls import patterns,url

urlpatterns = patterns('userauth.views',
                       url(r'^login/$','user_login',name='login'),
                       )

