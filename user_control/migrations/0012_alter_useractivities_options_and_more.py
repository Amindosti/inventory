# Generated by Django 4.1.7 on 2023-03-04 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0011_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useractivities',
            options={'ordering': ('-created_at1',)},
        ),
        migrations.RenameField(
            model_name='useractivities',
            old_name='created_at',
            new_name='created_at1',
        ),
        migrations.RenameField(
            model_name='useractivities',
            old_name='email',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='useractivities',
            old_name='fullname',
            new_name='fullname1',
        ),
    ]
