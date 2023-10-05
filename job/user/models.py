from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self ,  username, password, name,**kwargs):
        if not name:
            raise  ValueError("必须要传递姓名！")
        if not password:
            raise  ValueError("必须要传递密码")
        user = self.model( name = name, username= username , **kwargs)
        # user.set_password( password )
        user.save()
        return  user

    def create_user(self,   username, password,name, **kwargs):
        # kwargs['is_superuser'] = False
        return self._create_user(name=name, username=username, password = password, **kwargs )

    def create_superuser(self,  username, password, name,**kwargs):
        # kwargs['is_superuser'] = True
        return  self._create_user(name=name, username=username, password = password, **kwargs )


class Clazz(models.Model):
    clazz_name = models.CharField(max_length=32)
    def __str__(self):
        return self.clazz_name

class Status(models.Model):
    status_name = models.CharField(max_length=32, verbose_name='选择状态')
    def __str__(self):
        return self.status_name

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('A', '教师'),
        ('B', '学生'),
        ('1', '身份1'),
        ('2', '身份2'),
        ('3', '身份3'),
        ('4', '身份4'),
        ('5', '身份5'),
        ('6', '身份6'),
    )
    GENDER_CHOICES = (
        ('A', '男'),
        ('B', '女')
    )
    username = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32)
    level = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default='B')  # 根据定义选项来限制取值范围
    clazz = models.ForeignKey(to=Clazz, on_delete=models.CASCADE)
    phone = models.CharField(max_length=32, null=True, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True, blank=True)
    password = models.CharField(max_length=32, null=True, blank=True, default='123456')

    status = models.ForeignKey(to=Status, on_delete=models.CASCADE, null=True, blank=True,default=6)

    USERNAME_FIELD = "username"   #USERNAME_FIELD作用，是执行authenticate验证， username参数传入后，实际校验的是telephone字段
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username


class UserToken(models.Model):
    token = models.CharField(max_length=1000)
    uid = models.OneToOneField(to=User, on_delete=models.CASCADE)


class Company(models.Model):
    cname = models.CharField(verbose_name='公司名称', max_length=64)

    def __str__(self):
        return self.cname


class Job(models.Model):
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    jname = models.CharField(verbose_name='岗位', max_length=64)
    total_number = models.IntegerField(verbose_name='提供岗位数量')
    still_number = models.IntegerField(verbose_name='剩余岗位数量')
    des = models.TextField(null=True, blank=True)
    is_end = models.SmallIntegerField(max_length=2)

    def __str__(self):
        return self.jname


class Record(models.Model):
    sid = models.CharField(verbose_name='学号', max_length=64, unique=True)
    sname = models.CharField(verbose_name='姓名', max_length=64)
    clazz = models.ForeignKey(to=Clazz, on_delete=models.CASCADE)
    job = models.ForeignKey(to=Job, on_delete=models.CASCADE)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    mobile = models.CharField(verbose_name='电话号码', max_length=13)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='第一次选择时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最近一次更新时间')

    def __str__(self):
        return self.sname

