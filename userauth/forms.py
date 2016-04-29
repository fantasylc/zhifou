__author__ = 'liuchao'
#coding:utf-8

from django import forms

from .models import User

from django.core.mail import send_mail
from django.contrib.auth import authenticate


