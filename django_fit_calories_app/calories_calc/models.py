from django.db import models
from users.models import CustomUser


# Create your models here.
'''class Customer(CustomUser):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)'''

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


class FoodItem(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.ManyToManyField(Category)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='Углеводы')
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='Жиры')
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='Белки')
    calorie = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True, verbose_name='Калории')
    quantity = models.IntegerField(default=100, null=True, blank=True, verbose_name='Количество в граммах')

    def __str__(self):
        return str(self.name)

    # for user page-------------------------------------------------------------


class UserFoodItem(models.Model):
    customer = models.ManyToManyField(CustomUser)
    fooditem = models.ManyToManyField(FoodItem)
    category = models.ManyToManyField(Category)

