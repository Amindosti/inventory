# Generated by Django 4.1.7 on 2023-03-04 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0013_alter_useractivities_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
