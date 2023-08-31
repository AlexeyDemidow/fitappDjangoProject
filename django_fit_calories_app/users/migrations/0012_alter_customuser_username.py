# Generated by Django 4.2.3 on 2023-08-31 20:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует.'}, help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.', max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9]+$', message='Псевдоним может состоять только из латинских символов и цифр')], verbose_name='Имя пользователя'),
        ),
    ]
