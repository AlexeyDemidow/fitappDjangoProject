from django.forms import ModelForm
from .models import *
from users.models import CustomUser
from django import forms



class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'carbohydrate', 'fats', 'protein', 'calorie', 'quantity', 'category', 'date']


class AddUserFoodItem_breakfast(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='breakfast')

class AddUserFoodItem_lunch(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='lunch')

class AddUserFoodItem_dinner(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='dinner')

class AddUserFoodItem_snacks(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='snacks')