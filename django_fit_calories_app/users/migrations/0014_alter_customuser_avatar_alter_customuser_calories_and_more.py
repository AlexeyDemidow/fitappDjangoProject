# Generated by Django 4.2.3 on 2023-09-03 18:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='avatars/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='calories',
            field=models.IntegerField(default=0, help_text='Введите 0 чтобы рассчитать автоматически', validators=[django.core.validators.MinValueValidator(0, message='Калораж не может быть отрицательным')], verbose_name='Количество калорий в день'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Этот адрес электронной почты занят.'}, max_length=254, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='growth',
            field=models.IntegerField(default=0, help_text='Введите в сантиметрах', validators=[django.core.validators.MinValueValidator(0, message='Рост не может быть отрицательным')], verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким псевдонимом уже существует.'}, help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символ _', max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_]+$', message='Псевдоним может состоять только из латинских символов, цифр и символа _')], verbose_name='Псевдоним'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='weight',
            field=models.FloatField(default=0, help_text='Введите в килограммах', validators=[django.core.validators.MinValueValidator(0, message='Вес не может быть отрицательным')], verbose_name='Вес'),
        ),
    ]