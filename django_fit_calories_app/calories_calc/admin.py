# Register your models here.
from django.contrib import admin
from .models import *


# Модель еды в админ панели
class FoodAdmin(admin.ModelAdmin):
    class Meta:
        model = FoodItem

    list_display = ['name', 'carbohydrate', 'fats', 'protein', 'calorie', 'quantity']
    list_filter = ['name']


# Разделы в админ панели
admin.site.register(UserFoodItem)
admin.site.register(WaterTracker)
admin.site.register(Category)
admin.site.register(FoodItem, FoodAdmin)
