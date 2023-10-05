from django.db import models

# Create your models here.
class Class05Items(models.Model):
    item = models.CharField(max_length=32, verbose_name='项目名')
    vol_num = models.IntegerField(max_length=16, verbose_name='志愿者数量')
    player_num = models.IntegerField(max_length=16, verbose_name='运动员数量')
    tourist_num = models.IntegerField(max_length=16, verbose_name='游客数量')

    def __str__(self):
        return self.item


class Class05Source(models.Model):
    source = models.CharField(max_length=32, verbose_name='资源')
    num = models.IntegerField(max_length=16, verbose_name='剩余数量')

    def __str__(self):
        return self.source

class Class05Temp(models.Model):
    hour = models.IntegerField(max_length=32, verbose_name='小时')
    temp = models.FloatField(max_length=16, verbose_name='温度',)

    def __str__(self):
        return self.hour

class Class05Info(models.Model):
    player = models.IntegerField(max_length=32, verbose_name='选手数')
    volunteer = models.IntegerField(max_length=32, verbose_name='志愿者数')
    bus = models.IntegerField(max_length=32, verbose_name='接待车辆数')
    medic = models.IntegerField(max_length=32, verbose_name='医疗队数')


class Class05Province(models.Model):
    province = models.CharField(max_length=32, verbose_name='省份')
    gold_medal = models.IntegerField(max_length=16, verbose_name='金牌数')
    silver_medal = models.IntegerField(max_length=16, verbose_name='银牌数')
    bronze_medal = models.IntegerField(max_length=16, verbose_name='铜牌数')
    cctv = models.IntegerField(max_length=16, verbose_name='cctv观众数')
    douyin = models.IntegerField(max_length=16, verbose_name='抖音观众数')
    weixin = models.IntegerField(max_length=16, verbose_name='微信观众数')
    others = models.IntegerField(max_length=16, verbose_name='其他渠道观众数')

    def __str__(self):
        return self.province



class Class01Type(models.Model):
    year = models.IntegerField(max_length=32, verbose_name='年份')
    knx = models.IntegerField(max_length=16, verbose_name='康乃馨')
    yjx = models.IntegerField(max_length=16, verbose_name='郁金香')
    mg = models.IntegerField(max_length=16, verbose_name='玫瑰')
    xrk = models.IntegerField(max_length=16, verbose_name='向日葵')
    mtx = models.IntegerField(max_length=16, verbose_name='满天星')
    others = models.IntegerField(max_length=16, verbose_name='其他')

    def __str__(self):
        return self.year

class Class01Sales(models.Model):
    year = models.IntegerField(max_length=32, verbose_name='年份')
    month = models.IntegerField(max_length=16, verbose_name='月份')
    money = models.IntegerField(max_length=16, verbose_name='销售额')

class Class01Age(models.Model):
    age = models.CharField(max_length=32, verbose_name='年龄')
    money = models.IntegerField(max_length=16, verbose_name='销售额')

class Class01City(models.Model):
    city = models.CharField(max_length=32, verbose_name='年份')
    province = models.CharField(max_length=32, verbose_name='省份')
    money = models.IntegerField(max_length=16, verbose_name='销售额/万元')



class Class01Way(models.Model):
    way = models.CharField(max_length=32, verbose_name='渠道')
    money = models.IntegerField(max_length=16, verbose_name='销售额/万元')

class Class01Day(models.Model):
    day = models.CharField(max_length=32, verbose_name='日期')
    money = models.IntegerField(max_length=16, verbose_name='销售额/万元')


class Class08Store(models.Model):
    store = models.CharField(max_length=32, verbose_name='店名')
    drink = models.CharField(max_length=32, verbose_name='饮品名')
    sales_today = models.IntegerField(max_length=16, verbose_name='今日销量')
    sales_month = models.IntegerField(max_length=16, verbose_name='本月销量')
    volume_today = models.IntegerField(max_length=16, verbose_name='今日销量')
    volume_month = models.IntegerField(max_length=16, verbose_name='本月销量')

    def __str__(self):
        return self.store


class Class08Month(models.Model):
    store = models.CharField(max_length=32, verbose_name='店名')
    money = models.TextField(verbose_name='每天金额')



class Class02Player(models.Model):
    game = models.CharField(max_length=32, verbose_name='游戏名')
    free_player = models.CharField(max_length=32, verbose_name='空闲打手数')
    active_player = models.IntegerField(max_length=16, verbose_name='活跃打手数')
    sales = models.IntegerField(max_length=16, verbose_name='今日销售额')
    finish_order = models.IntegerField(max_length=16, verbose_name='完成订单数')
    unfinish_order = models.IntegerField(max_length=16, verbose_name='未完成订单数')

    def __str__(self):
        return self.game


class Class02Sales(models.Model):
    finish_order = models.IntegerField(max_length=32, verbose_name='本月成单量')
    total_order = models.CharField(max_length=32, verbose_name='本月接单量')
    girl_order_rate = models.IntegerField(max_length=16, verbose_name='女生接单率')
    girl_sales_rate = models.IntegerField(max_length=16, verbose_name='女生销售额占比')
    inquiry_today = models.IntegerField(max_length=16, verbose_name='今日询盘量')
    inquiry_month = models.IntegerField(max_length=16, verbose_name='本月询盘量')


class Class06Spot(models.Model):
    spot = models.CharField(max_length=32, verbose_name='景区')
    kid = models.IntegerField(max_length=32, verbose_name='儿童')
    adult = models.IntegerField(max_length=16, verbose_name='青年')
    old = models.IntegerField(max_length=16, verbose_name='老人')

    def __str__(self):
        return self.spot