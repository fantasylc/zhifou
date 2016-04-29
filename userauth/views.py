from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
import json
from .models import User
import uuid
from .others import sendconfirmemail
from django.contrib import messages

def user_login(request):
    if request.method == "POST":

        try:
            email = request.POST.get('email','')
            password = request.POST.get('password','')
            user = authenticate(email=email,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    info = {'status':'success','message':'登录成功'}
                    return HttpResponse(json.dumps(info))
                else:
                    return HttpResponse(json.dumps({'status':'failure','message':'邮箱还没有验证,请验证你的邮箱!'}))

            else:
                info = {'status':'failure','message':'用户名或密码错误'}
                return HttpResponse(json.dumps(info))

        except Exception as e:
            return HttpResponse(json.dumps({'status':'failture','message':'登录异常,请再试一次!'}))


def user_logout(request):
    try:
        logout(request)
        return HttpResponse('注销成功!')
    except Exception as e:
        return HttpResponse('注销异常')


def user_register(request):
    if request.method == 'POST':
        errors = []
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        name = email.split('@')[0]
        active_code = str(uuid.uuid5(uuid.NAMESPACE_DNS,email))
        user = User.objects.filter(email=email)
        if user:
            if user.is_active:
                return HttpResponse(json.dumps({'status':'failure','message':'邮箱已注册，请直接登陆或用其他邮箱注册！'}))
            #return HttpResponse(user)
            else:
                return HttpResponse(json.dumps({'status':'failure','message':'邮箱已经注册,请验证邮箱!'}))
        try:
            sendconfirmemail(email=email,active_code=active_code)


        except Exception as e:
            return HttpResponse('邮件发送出错，注册失败!',status=500)

        User.objects.create_user(email,password=password,name=name,active_code=active_code)
        return HttpResponse(json.dumps({'status':'success','message':'验证邮件已发送给你,请查收验证邮箱!'}))

def user_active(request,active_code):
    try:
        user = User.objects.get(active_code=active_code)
        if user:
            user.is_active=True
            user.save()
            user = authenticate(email=user.email,active_code=active_code)
            if user.is_active:
                login(request,user)
                messages.success(request,"你的邮箱已经验证成功!")
                return HttpResponseRedirect('/')

        return HttpResponseNotFound('<h1>Page not found</h1>')
    except:
        return HttpResponseNotFound('<h2>没有查找到用户!</h2>')











