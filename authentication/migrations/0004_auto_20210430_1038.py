# Generated by Django 3.2 on 2021-04-30 01:38

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, error_messages={'unique': 'this email is already exists.'}, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator]),
        ),
    ]