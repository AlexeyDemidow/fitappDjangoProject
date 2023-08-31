# Generated by Django 4.2.3 on 2023-08-31 17:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_weighing_weight_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует.'}, help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.', max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', message='Псевдоним может состоять только из латинских символов')], verbose_name='Имя пользователя'),
        ),
    ]