from django.forms import ModelForm
from .models import *
from users.models import CustomUser
from django import forms



class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'carbohydrate', 'fats', 'protein', 'calorie', 'quantity']


class AddUserFoodItem(ModelForm):

    #customer = forms.ModelChoiceField(queryset=CustomUser.objects.all())

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem']

