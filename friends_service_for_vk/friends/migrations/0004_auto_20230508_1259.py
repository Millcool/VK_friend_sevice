# Generated by Django 3.2.19 on 2023-05-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_auto_20230506_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendship',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='user',
        ),
        migrations.AddField(
            model_name='friendship',
            name='friend_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='friendship',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
