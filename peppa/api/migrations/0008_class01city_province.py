# Generated by Django 3.2 on 2023-05-19 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_class01day_class01way'),
    ]

    operations = [
        migrations.AddField(
            model_name='class01city',
            name='province',
            field=models.CharField(default=1, max_length=32, verbose_name='省份'),
            preserve_default=False,
        ),
    ]
