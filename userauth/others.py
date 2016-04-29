__author__ = 'liuchao'
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context,loader

def sendconfirmemail(email=None,active_code=None):
    title = '欢迎注册知否!'
    subject,from_email,to = title,settings.EMAIL_HOST_USER,email
    active_address = 'http://127.0.0.1:8000/userauth/confirm/'+active_code+'/'
    html = loader.get_template('email/confirm_email.html')
    context = {'active_address':active_address}
    html_content = html.render(Context(context))
    msg = EmailMultiAlternatives(subject,html_content,from_email,(to,))
    msg.attach_alternative(html_content,'text/html')
    msg.send()



