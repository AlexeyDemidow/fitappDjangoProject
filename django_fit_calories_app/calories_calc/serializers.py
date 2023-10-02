from rest_framework import serializers

from users.models import CustomUser
from .models import FoodItem, UserFoodItem, Category


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id', 'name', 'calorie', 'protein', 'fats', 'carbohydrate', 'quantity')


class UserFoodItemSerializerRead(serializers.ModelSerializer):
    customer = serializers.CharField(source='customer__username')
    fooditem = serializers.CharField(source='fooditem__name')
    category = serializers.CharField(source='category__name')

    class Meta:
        model = UserFoodItem
        fields = ['id', 'customer', 'fooditem', 'category', 'add_date', 'quantity']


class UserFoodItemSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = UserFoodItem
        fields = ['id', 'customer', 'fooditem', 'category', 'add_date', 'quantity']
