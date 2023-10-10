from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from PIL import Image
from django.utils import timezone
from django.core.validators import RegexValidator, MinValueValidator, EmailValidator


# Модель пользователя
class CustomUser(AbstractUser):

    username_validator = RegexValidator(
        r'^[a-zA-Z0-9_]+$',
        message='Псевдоним может состоять только из латинских символов, цифр и символа _'
    )

    username = models.CharField(
        'Псевдоним',
        max_length=150,
        unique=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символ _',
        validators=[username_validator],
        error_messages={
            'unique': 'Пользователь с таким псевдонимом уже существует.',
        },
    )

    email = models.EmailField(
        'Адрес электронной почты',
        unique=True,
        validators=[EmailValidator],
        error_messages={
            'unique': 'Этот адрес электронной почты занят.',
        },
    )

    man = 'Мужской'
    woman = 'Женский'
    gender_list = [(man, man), (woman, woman)]
    gender = models.CharField(max_length=10, choices=gender_list, default=man, verbose_name='Пол')

    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения',
        help_text='Введите в формате ДД.ММ.ГГГГ',
    )

    growth_validator = MinValueValidator(0, message='Рост не может быть отрицательным')
    growth = models.IntegerField(
        default=0,
        verbose_name='Рост',
        help_text='Введите в сантиметрах',
        validators=[growth_validator],
    )

    weight_validator = MinValueValidator(0, message='Вес не может быть отрицательным')
    weight = models.FloatField(
        default=0,
        verbose_name='Вес',
        help_text='Введите в килограммах',
        validators=[weight_validator],
    )

    avatar = models.ImageField(default='default.png', upload_to='avatars/', verbose_name='Аватар',)

    low = 'Минимальный'
    weak = 'Слабый'
    mid = 'Умеренный'
    high = 'Тяжелый'
    extreme = 'Экстремальный'
    activity_list = [
        (low, low),
        (weak, weak),
        (mid, mid),
        (high, high),
        (extreme, extreme),
    ]
    activity = models.CharField(
        max_length=100,
        choices=activity_list,
        default=low,
        verbose_name='Уровень активности',
        help_text='Выберите ваш уровень активности.',
    )

    calories_validator = MinValueValidator(0, message='Калораж не может быть отрицательным')
    calories = models.IntegerField(
        default=0,
        verbose_name='Количество калорий в день',
        help_text='Введите 0 чтобы рассчитать автоматически',
        validators=[calories_validator],
    )

    # Функция сохранения профиля
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.avatar:
            self.avatar = 'default.png'
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

    # Вычисление нормы калорий в день
    def calories_per_day(self):
        today = datetime.now().date()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month,
                                                                               self.birth_date.day))
        result_m = ((10 * int(self.weight)) + (6.25 * int(self.growth)) - (5 * int(age)) + 5)
        result_w = ((10 * int(self.weight)) + (6.25 * int(self.growth)) - (5 * int(age)) - 161)

        if self.gender == 'Мужской':
            if self.activity == self.low:
                result_m *= 1.2
            if self.activity == self.weak:
                result_m *= 1.375
            if self.activity == self.mid:
                result_m *= 1.55
            if self.activity == self.high:
                result_m *= 1.7
            if self.activity == self.extreme:
                result_m *= 1.9
            return round(result_m)

        if self.gender == 'Женский':
            if self.activity == self.low:
                result_w *= 1.2
            if self.activity == self.weak:
                result_w *= 1.375
            if self.activity == self.mid:
                result_w *= 1.55
            if self.activity == self.high:
                result_w *= 1.7
            if self.activity == self.extreme:
                result_w *= 1.9
            return round(result_w)

    # Вычисление коэффициента массы тела
    def body_mass_ratio(self):
        result = int(self.weight) / (int(self.growth) / 100) ** 2
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

    REQUIRED_FIELDS = ['email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar', 'calories']


# Модель отвечающая за взвешивание пользователя
class Weighing(models.Model):
    weighing_date = models.DateField(default=timezone.now, verbose_name='Дата взвешивания')
    weight_value = models.FloatField(default=0, verbose_name='Вес', help_text='Введите в килограммах')
    user = models.ManyToManyField(CustomUser)

    def __str__(self):
        return str([i.get('username') for i in self.user.values('username')][0])
