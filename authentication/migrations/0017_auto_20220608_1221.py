# Generated by Django 3.1.3 on 2022-06-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0016_auto_20220607_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='assets/images/avatar.png', null=True, upload_to='user/'),
        ),
    ]
