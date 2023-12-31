# Generated by Django 3.2 on 2023-05-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_class05source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class05Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.IntegerField(max_length=32, verbose_name='小时')),
                ('temp', models.FloatField(max_length=16, verbose_name='温度')),
            ],
        ),
        migrations.AlterField(
            model_name='class05source',
            name='num',
            field=models.IntegerField(max_length=16, verbose_name='剩余数量'),
        ),
        migrations.AlterField(
            model_name='class05source',
            name='source',
            field=models.CharField(max_length=32, verbose_name='资源'),
        ),
    ]
