# Generated by Django 3.2 on 2023-06-15 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_job_id_end'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='id_end',
            new_name='is_end',
        ),
    ]
