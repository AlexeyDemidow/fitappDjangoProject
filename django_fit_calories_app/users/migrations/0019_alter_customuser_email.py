# Generated by Django 4.2.3 on 2023-09-03 18:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Этот адрес электронной почты занят.'}, max_length=254, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='Адрес электронной почты'),
        ),
    ]
