# Generated by Django 3.2 on 2023-05-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20230523_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class05Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=32, verbose_name='项目名')),
                ('num', models.IntegerField(max_length=16, verbose_name='志愿者数量')),
            ],
        ),
    ]
