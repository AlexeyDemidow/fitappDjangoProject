from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime
from PIL import Image

# Create your models here.


class CustomUser(AbstractUser):
    man = 'Мужской'
    woman = 'Женский'
    gender_list = [(man, 'Мужской'), (woman, 'Женский')]
    gender = models.CharField(max_length=10, choices=gender_list, default=man, verbose_name='Пол')

    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения', help_text='Введите в формате ДД.ММ.ГГГГ')
    growth = models.IntegerField(default=0, verbose_name='Рост', help_text='Введите в сантиметрах')
    weight = models.IntegerField(default=0, verbose_name='Вес', help_text='Введите в килограммах')
    avatar = models.ImageField(default='default.png', upload_to='avatars/', blank=True, verbose_name='Аватар')

    low = 'Минимальный'
    weak = 'Слабый'
    mid = 'Умеренный'
    high = 'Тяжелый'
    extreme = 'Экстремальный'
    activity_list = [(low, 'Минимальный'), (weak, 'Слабый'), (mid, 'Умеренный'), (high, 'Тяжелый'), (extreme, 'Экстремальный')]
    activity = models.CharField(max_length=100, choices=activity_list, default=low, verbose_name='Уровень активности', help_text='Выберите ваш уровень активности.')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

    '''def get_user_age(user):
        today = datetime.now().date()
        age = today.year - user.birth_date.year - ((today.month, today.day) < (user.birth_date.month, user.birth_date.day))
        return age'''


    def calories_per_day(user):
        today = datetime.now().date()
        age = today.year - user.birth_date.year - ((today.month, today.day) < (user.birth_date.month, user.birth_date.day))
        if user.gender == 'Мужской':
            if user.activity == 'Минимальный':
                result = ((10 * int(user.weight)) + (6.25 * int(user.growth)) - (5 * int(age)) + 5) * 1.2
                return round(result)
            if user.activity == 'Слабый':
                result = ((10 * int(user.weight)) + (6.25 * int(user.growth)) - (5 * int(age)) + 5) * 1.375
                return round(result)
            if user.activity == 'Умеренный':
                result = ((10 * int(user.weight)) + (6.25 * int(user.growth)) - (5 * int(age)) + 5) * 1.55
                return round(result)
            if user.activity == 'Тяжелый':
                result = ((10 * int(user.weight)) + (6.25 * int(user.growth)) - (5 * int(age)) + 5) * 1.7
                return round(result)
            if user.activity == 'Экстремальный':
                result = ((10 * int(user.weight)) + (6.25 * int(user.growth)) - (5 * int(age)) + 5) * 1.9
                return round(result)

        if user.gender == 'Женский':
            if user.activity == 'Минимальный':
                result = ((10 * int(user.weight)) + (6.25 * int(user.growth)) - (5 * int(age)) - 161) * 1.2
                return round(result)
            if user.activity == 'Слабый':
                result = ((10 * int(user.weight)) + (6.25 * int(user.growth)) - (5 * int(age)) - 161) * 1.375
                return round(result)
            if user.activity == 'Умеренный':
                result = ((10 * int(user.weight)) + (6.25 * int(user.growth)) - (5 * int(age)) - 161) * 1.55
                return round(result)
            if user.activity == 'Тяжелый':
                result = ((10 * int(user.weight)) + (6.25 * int(user.growth)) - (5 * int(age)) - 161) * 1.7
                return round(result)
            if user.activity == 'Экстремальный':
                result = ((10 * int(user.weight)) + (6.25 * int(user.growth)) - (5 * int(age)) - 161) * 1.9
                return round(result)
