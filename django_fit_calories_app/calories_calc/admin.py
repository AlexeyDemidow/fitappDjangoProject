from django.contrib import admin
from .models import *


class FoodAdmin(admin.ModelAdmin):
    """Модель еды в админ-панели"""

    class Meta:
        model = FoodItem

    list_display = ['name', 'carbohydrate', 'fats', 'protein', 'calorie', 'quantity']
    list_filter = ['name', 'carbohydrate', 'fats', 'protein', 'calorie']


class UserFoodAdmin(admin.ModelAdmin):
    """Модель пользовательской пищи в админ-панели"""

    class Meta:
        model = UserFoodItem

    list_display = ['_fooditem', 'quantity', '_customer',  '_category', 'add_date']
    list_filter = ['customer',  'category', 'add_date']

    def _customer(self, row):
        return ','.join([x.username for x in row.customer.all()])

    def _fooditem(self, row):
        return ','.join([x.name for x in row.fooditem.all()])

    def _category(self, row):
        return ','.join([x.name for x in row.category.all()])


class WaterTrackerAdmin(admin.ModelAdmin):
    """Модель трекера воды в админ панели"""

    class Meta:
        model = WaterTracker

    list_display = ['_customer', 'glass', 'drink_date']
    list_filter = ['customer', 'glass', 'drink_date']

    def _customer(self, row):
        return ','.join([x.username for x in row.customer.all()])


admin.site.register(UserFoodItem, UserFoodAdmin)
admin.site.register(WaterTracker, WaterTrackerAdmin)
admin.site.register(FoodItem, FoodAdmin)
