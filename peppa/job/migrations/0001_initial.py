# Generated by Django 3.2 on 2023-06-11 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clazz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clazz', models.CharField(max_length=64, verbose_name='班级')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=64, verbose_name='公司名称')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jname', models.CharField(max_length=64, verbose_name='岗位')),
                ('total_number', models.IntegerField(verbose_name='提供岗位数量')),
                ('still_number', models.IntegerField(verbose_name='剩余岗位数量')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.company')),
            ],
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('uid', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('user_type', models.CharField(choices=[('A', '教师'), ('B', '学生')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User1Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='job.user1')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=64, unique=True, verbose_name='学号')),
                ('sname', models.CharField(max_length=64, verbose_name='姓名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='第一次选择时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最近一次更新时间')),
                ('clazz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.clazz')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.company')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
        ),
    ]
