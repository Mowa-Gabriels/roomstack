# Generated by Django 3.1.3 on 2022-05-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iroomie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(max_length=225),
        ),
    ]
