from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# 学生信息表
class Student(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    age = models.IntegerField(verbose_name='年龄', max_length=16)
    GENDER_CHOICES = [
        (1, '男'),
        (2, '女'),
        (0, '不详'),
    ]
    gender = models.SmallIntegerField(max_length=1, choices=GENDER_CHOICES, verbose_name='性别')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=32)


class User1(models.Model):
    USER_TYPE_CHOICES = (
        ('A', '管理员'),
        ('B', 'Vip用户'),
        ('C', '普通用户'),
    )
    uid = models.CharField(max_length=16, primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)  # 根据定义选项来限制取值范围

    def set_password(self, password):
        self.password = make_password(password)  # 使用Django提供的密码加密方式

    def check_password(self, password):
        return check_password(password, self.password)  # 判断密码是否匹配



class User1Token(models.Model):
    token = models.CharField(max_length=64)
    user = models.OneToOneField(to=User1, on_delete=models.CASCADE)

# # 用户表
# class User(models.Model):
#     USER_TYPE = (
#         (1, '超级用户'),
#         (2, 'VIP用户'),
#         (3, '普通用户')
#     )
#     username = models.CharField(max_length=32)
#     name = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#     user_type = models.IntegerField(choices=USER_TYPE)
#
#     class Meta:
#         ...
#
#     def __str__(self):
#         return self.name
#
#
# # 用户Token表
# class UserToken(models.Model):
#     token = models.CharField(max_length=64)
#     user = models.OneToOneField(to=User, on_delete=models.CASCADE)
