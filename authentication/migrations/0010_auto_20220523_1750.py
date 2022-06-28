# Generated by Django 3.1.3 on 2022-05-24 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20220517_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='school',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sex',
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.school'),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer not to specify', 'Prefer not to specify')], max_length=225, null=True),
        ),
    ]
