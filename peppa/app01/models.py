from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=255, help_text='学生姓名')
    age = models.IntegerField(verbose_name='年龄', help_text='年龄')
    gender = models.SmallIntegerField(verbose_name='性别', max_length=5, choices=((1,'男'),(0,'女')))

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name
        ordering = ('name',)

    def __str__(self):
        return self.name
