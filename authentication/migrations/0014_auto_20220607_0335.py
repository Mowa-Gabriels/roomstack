# Generated by Django 3.1.3 on 2022-06-07 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_auto_20220606_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='user/avatar.png', null=True, upload_to='user/'),
        ),
    ]