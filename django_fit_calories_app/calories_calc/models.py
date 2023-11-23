from django.db import models
from users.models import CustomUser
from django.utils import timezone


class Category(models.Model):
    """Категории продуктов"""

    options = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snacks', 'snacks'),
    )
    name = models.CharField(max_length=50, choices=options)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    """Модель пищи"""

    name = models.CharField(max_length=200, verbose_name='Название')
    carbohydrate = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Углеводы')
    fats = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Жиры')
    protein = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Белки')
    calorie = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Калории')
    quantity = models.IntegerField(default=100, null=True, blank=True, verbose_name='Количество в граммах')

    def __str__(self):
        return str(self.name)


class UserFoodItem(models.Model):
    """Модель пищи пользователя"""

    customer = models.ManyToManyField(CustomUser, verbose_name='Пользователь')
    fooditem = models.ManyToManyField(FoodItem, verbose_name='Еда')
    category = models.ManyToManyField(Category, verbose_name='Категория')
    add_date = models.DateField(default=timezone.now, verbose_name='Дата')
    quantity = models.IntegerField(default=100, null=True, blank=True, verbose_name='Количество в граммах')

    def __str__(self):
        return str([i.get('name') for i in self.fooditem.values('name')][0])


class ChooseDate(models.Model):
    """Выбор даты"""

    c_date = models.DateField(default=timezone.now, verbose_name='Дата')
    customer = models.ManyToManyField(CustomUser)


class WaterTracker(models.Model):
    """Трекер воды"""

    customer = models.ManyToManyField(CustomUser)
    glass = models.IntegerField(default=1, null=True, blank=True, verbose_name='Стаканы, 1 стакан = 250г воды')
    drink_date = models.DateField(default=timezone.now, verbose_name='Дата')

    def __str__(self):
        return str([i.get('username') for i in self.customer.values('username')][0])
