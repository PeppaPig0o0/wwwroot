# Generated by Django 3.2 on 2023-05-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class05items',
            name='tourist_num',
            field=models.IntegerField(default=825, max_length=16, verbose_name='游客数量'),
            preserve_default=False,
        ),
    ]
