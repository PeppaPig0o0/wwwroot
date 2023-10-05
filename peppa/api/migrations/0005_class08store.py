# Generated by Django 3.2 on 2023-05-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_class01type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class08Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=32, verbose_name='店名')),
                ('drink', models.CharField(max_length=32, verbose_name='饮品名')),
                ('sales_today', models.IntegerField(max_length=16, verbose_name='今日销量')),
                ('sales_month', models.IntegerField(max_length=16, verbose_name='本月销量')),
                ('volume_today', models.IntegerField(max_length=16, verbose_name='今日销量')),
                ('volume_month', models.IntegerField(max_length=16, verbose_name='本月销量')),
            ],
        ),
    ]
