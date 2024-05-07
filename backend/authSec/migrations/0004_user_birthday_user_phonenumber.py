# Generated by Django 4.2.7 on 2024-04-23 08:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authSec', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(default='', max_length=20),
        ),
    ]
