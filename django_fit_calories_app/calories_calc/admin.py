from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


# Now, Register the models here.

class FoodAdmin(admin.ModelAdmin):
    class Meta:
        model = FoodItem

    list_display = ['name', 'carbohydrate', 'fats', 'protein', 'calorie', 'quantity']
    list_filter = ['name']




admin.site.register(UserFoodItem)
admin.site.register(Category)
admin.site.register(FoodItem, FoodAdmin)
