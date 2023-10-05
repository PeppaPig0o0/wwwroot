# Generated by Django 3.2 on 2023-05-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_class01age_class01city_class01sales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class01Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=32, verbose_name='日期')),
                ('money', models.IntegerField(max_length=16, verbose_name='销售额/万元')),
            ],
        ),
        migrations.CreateModel(
            name='Class01Way',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(max_length=32, verbose_name='渠道')),
                ('money', models.IntegerField(max_length=16, verbose_name='销售额/万元')),
            ],
        ),
    ]
