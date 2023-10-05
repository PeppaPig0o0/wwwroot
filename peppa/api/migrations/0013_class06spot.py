# Generated by Django 3.2 on 2023-05-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20230523_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class06Spot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot', models.CharField(max_length=32, verbose_name='景区')),
                ('kid', models.IntegerField(max_length=32, verbose_name='儿童')),
                ('adult', models.IntegerField(max_length=16, verbose_name='青年')),
                ('old', models.IntegerField(max_length=16, verbose_name='老人')),
            ],
        ),
    ]
