__author__ = 'liuchao'
from django.conf.urls import patterns,url
from django.conf import settings

urlpatterns = patterns('userauth.views',
                       url(r'^login/$','user_login',name='login'),
                       url(r'^register/$','user_register',name='register'),
                       url(r'^logout/$','user_logout',name='loginout'),
                       url(r'^confirm/(?P<active_code>.+)/$','user_active'),
                       )
