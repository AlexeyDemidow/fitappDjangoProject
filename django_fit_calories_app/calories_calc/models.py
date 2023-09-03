from django.db import models
from users.models import CustomUser
from django.utils import timezone


# Модель категории в которую будет распределен продукт
class Category(models.Model):
    options = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snacks', 'snacks'),
    )
    name = models.CharField(max_length=50, choices=options)

    def __str__(self):
        return self.name


# Модель еды
class FoodItem(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.ManyToManyField(Category, blank=True)
    carbohydrate = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Углеводы')
    fats = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Жиры')
    protein = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Белки')
    calorie = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Калории')
    quantity = models.IntegerField(default=100, null=True, blank=True, verbose_name='Количество в граммах')

    def __str__(self):
        return str(self.name)


# Модель пользовательской еды, состоит из названия еды, к какому пользователю относится, к какой категории относится,
# даты добавления и количества грамм
class UserFoodItem(models.Model):
    customer = models.ManyToManyField(CustomUser)
    fooditem = models.ManyToManyField(FoodItem)
    category = models.ManyToManyField(Category)
    add_date = models.DateField(default=timezone.now, verbose_name='Дата')
    quantity = models.IntegerField(default=100, null=True, blank=True, verbose_name='Количество в граммах')


# Модель выбора даты
class ChooseDate(models.Model):
    c_date = models.DateField(default=timezone.now, verbose_name='Дата')


# Модель трекера воды
class WaterTracker(models.Model):
    customer = models.ManyToManyField(CustomUser)
    glass = models.IntegerField(default=1, null=True, blank=True, verbose_name='1 стакан = 250г воды')
    drink_date = models.DateField(default=timezone.now, verbose_name='Дата')
