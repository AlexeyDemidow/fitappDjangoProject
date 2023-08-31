from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from PIL import Image
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.


class CustomUser(AbstractUser):

    username_validator = RegexValidator(r'^[a-zA-Z0-9]+$', message='Псевдоним может состоять только из латинских символов и цифр')
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
        validators=[username_validator],
        error_messages={
            'unique': 'Пользователь с таким именем уже существует.',
        },
    )

    man = 'Мужской'
    woman = 'Женский'
    gender_list = [(man, 'Мужской'), (woman, 'Женский')]
    gender = models.CharField(max_length=10, choices=gender_list, default=man, verbose_name='Пол')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения',
                                  help_text='Введите в формате ДД.ММ.ГГГГ')

    growth = models.IntegerField(default=0, verbose_name='Рост', help_text='Введите в сантиметрах')
    weight = models.FloatField(default=0, verbose_name='Вес', help_text='Введите в килограммах')

    avatar = models.ImageField(default='default.png', upload_to='avatars/', blank=True, verbose_name='Аватар')
    low = 'Минимальный'
    weak = 'Слабый'
    mid = 'Умеренный'
    high = 'Тяжелый'
    extreme = 'Экстремальный'
    activity_list = [(low, 'Минимальный'), (weak, 'Слабый'), (mid, 'Умеренный'), (high, 'Тяжелый'),
                     (extreme, 'Экстремальный')]
    activity = models.CharField(max_length=100, choices=activity_list, default=low, verbose_name='Уровень активности',
                                help_text='Выберите ваш уровень активности.')
    calories = models.IntegerField(default=0, verbose_name='Количество калорий в день', help_text='Введите 0 чтобы рассчитать автоматически')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)



    def calories_per_day(user):
        today = datetime.now().date()
        age = today.year - user.birth_date.year - ((today.month, today.day) < (user.birth_date.month,
                                                                               user.birth_date.day))

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

    def body_mass_ratio(user):
        result = int(user.weight) / (int(user.growth) / 100) ** 2
        text_result = None
        if result <= 16:
            text_result = 'Выраженный дефицит массы тела'
        if 16 < result <= 18.5:
            text_result = 'Недостаточная (дефицит) масса тела'
        if 18.5 < result <= 25:
            text_result = 'Норма'
        if 25 < result <= 30:
            text_result = 'Избыточная масса тела (предожирение)'
        if 30 < result <= 35:
            text_result = 'Ожирение первой степени'
        if 35 < result <= 40:
            text_result = 'Ожирение второй степени'
        if 40 < result <= 99:
            text_result = 'Ожирение третьей степени'
        return round(result, 2), text_result



class Weighing(models.Model):
    weighing_date = models.DateField(default=timezone.now, verbose_name='Дата взвешивания')
    weight_value = models.FloatField(default=0, verbose_name='Вес', help_text='Введите в килограммах')
    user = models.ManyToManyField(CustomUser)
