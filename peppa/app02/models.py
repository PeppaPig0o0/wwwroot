from django.db import models

# Create your models here.
class Clazz(models.Model):
    name = models.CharField(max_length=32, verbose_name='班级名')



class Student(models.Model):
    name = models.CharField(max_length=32, verbose_name='学生姓名')
    clazz = models.ForeignKey(Clazz, on_delete=models.CASCADE)