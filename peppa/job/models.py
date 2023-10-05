from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    cname = models.CharField(verbose_name='公司名称', max_length=64)

    def __str__(self):
        return self.cname


class Job(models.Model):
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    jname = models.CharField(verbose_name='岗位', max_length=64)
    total_number = models.IntegerField(verbose_name='提供岗位数量')
    still_number = models.IntegerField(verbose_name='剩余岗位数量')

    def __str__(self):
        return self.jname

class Clazz(models.Model):
    clazz = models.CharField(verbose_name='班级', max_length=64)
    def __str__(self):
        return self.clazz

class Record(models.Model):
    sid = models.CharField(verbose_name='学号', max_length=64, unique=True)
    sname = models.CharField(verbose_name='姓名', max_length=64)
    clazz = models.ForeignKey(to=Clazz, on_delete=models.CASCADE)
    job = models.ForeignKey(to=Job, on_delete=models.CASCADE)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='第一次选择时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最近一次更新时间')

    def __str__(self):
        return self.sname


class User(models.Model):
    USER_TYPE_CHOICES = (
        ('A', '教师'),
        ('B', '学生'),
    )
    username = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=32)
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)  # 根据定义选项来限制取值范围


# class User(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('A', '教师'),
#         ('B', '学生'),
#     )
#     username = models.CharField(max_length=16, primary_key=True)
#     name = models.CharField(max_length=32)
#     user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)  # 根据定义选项来限制取值范围
#

class UserToken(models.Model):
    token = models.CharField(max_length=1000)
    uid = models.OneToOneField(to=User, on_delete=models.CASCADE)



