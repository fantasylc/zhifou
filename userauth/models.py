#encoding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
# Create your models here.

SEX = {
    'man':'男',
    'women':'女',
}

PROFESSIONS = {

}

EDUCERT = {

}


class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError('注册必须使用邮箱!')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)

        if kwargs:
            if kwargs.get('active_code',None):
                user.active_code=kwargs['active_code']
            if kwargs.get('name',None):
                user.username = kwargs['name']

        user.save(using=self._db)


        return user

    def create_superuser(self,email,password,**kwargs):
        user = self.create_user(email,password=password)
        user.is_admin = True
        #user.is_staff=True
        user.is_active=True
        #user.is_superuser = True

        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='邮箱',max_length=255,unique=True)
    name = models.CharField(max_length=30, default='改个昵称吧', verbose_name='昵称')
    avatar = models.ImageField(upload_to='avatars', verbose_name='头像')
    sex = models.CharField(max_length=10, default='man', choices=SEX.items(), verbose_name='性别')
    jianjie = models.CharField(max_length=100, default='', verbose_name='简介')
    motto = models.CharField(max_length=100, default='', verbose_name='座右铭')
    profession = models.CharField(max_length=30, default='', choices=PROFESSIONS.items(), verbose_name='行业')
    city = models.CharField(max_length=20, default='', verbose_name='城市')
    school = models.CharField(max_length=20, default='', verbose_name='毕业学校')
    educert = models.CharField(max_length=10, default='', choices=EDUCERT.items(), verbose_name='学历')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    follower = models.ManyToManyField('self',symmetrical=False,related_name='followed',verbose_name='关注者')
    is_active = models.BooleanField(default=False,verbose_name='是否激活')


    active_code = models.CharField(max_length=200,default='',verbose_name='激活码')
    #is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']



    objects = MyUserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin



    class Meta:
        verbose_name_plural = verbose_name = '用户'
        ordering = ['-addtime']


    def __str__(self):
        return self.email


