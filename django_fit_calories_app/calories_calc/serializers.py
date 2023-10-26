from rest_framework import serializers

from .models import FoodItem, UserFoodItem, WaterTracker


# Сериалайзер базы данных продуктов
class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id', 'name', 'calorie', 'protein', 'fats', 'carbohydrate', 'quantity')


# Сериалайзер базы данных продуктов для чтения
class UserFoodItemSerializerRead(serializers.ModelSerializer):
    customer = serializers.CharField(source='customer__username')
    fooditem_name = serializers.CharField(source='fooditem__name')
    fooditem_protein = serializers.CharField(source='fooditem__protein')
    fooditem_fats = serializers.CharField(source='fooditem__fats')
    fooditem_carbohydrate = serializers.CharField(source='fooditem__carbohydrate')
    fooditem_calorie = serializers.CharField(source='fooditem__calorie')
    category = serializers.CharField(source='category__name')

    class Meta:
        model = UserFoodItem
        fields = ['id', 'customer', 'fooditem_name', 'fooditem_protein', 'fooditem_fats', 'fooditem_carbohydrate', 'fooditem_calorie', 'category', 'add_date', 'quantity']


# Сериалайзер базы данных продуктов для редактирования
class UserFoodItemSerializerWrite(serializers.ModelSerializer):
    # customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UserFoodItem
        fields = ['id', 'customer', 'fooditem', 'category', 'add_date', 'quantity']


# Сериалайзер трекера воды
class WaterTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterTracker
        fields = ['customer', 'glass', 'drink_date']