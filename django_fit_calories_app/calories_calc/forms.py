from django.forms import ModelForm
from .models import *
from users.models import CustomUser
from datetime import datetime
from django import forms


# Форма еды
class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calorie', 'protein', 'fats', 'carbohydrate', 'quantity']


# Форма добавления еды к завтраку
class AddUserFoodItemBreakfast(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    # Заполнение полей по умолчанию
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='breakfast')
        self.fields['add_date'].initial = datetime.now().date()


# Форма добавления еды обеду
class AddUserFoodItemLunch(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    # Заполнение полей по умолчанию
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='lunch')
        self.fields['add_date'].initial = datetime.now().date()


# Форма добавления еды ужину
class AddUserFoodItemDinner(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    # Заполнение полей по умолчанию
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='dinner')
        self.fields['add_date'].initial = datetime.now().date()


# Форма добавления еды перекусам
class AddUserFoodItemSnacks(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    # Заполнение полей по умолчанию
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='snacks')
        self.fields['add_date'].initial = datetime.now().date()


# Форма выбора даты
class ChooseDateForm(ModelForm):

    class Meta:
        model = ChooseDate
        fields = ['c_date', 'customer']

    # Заполнение полей по умолчанию
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])


# Форма трекера воды
class WaterTrackerFormPlus(ModelForm):

    class Meta:
        model = WaterTracker
        fields = ['glass', 'drink_date', 'customer']

    # Заполнение полей по умолчанию
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['drink_date'].initial = datetime.now().date()
        self.fields['glass'].initial = 1


class WaterTrackerFormMinus(ModelForm):

    class Meta:
        model = WaterTracker
        fields = ['glass', 'drink_date', 'customer']

    # Заполнение полей по умолчанию
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['drink_date'].initial = datetime.now().date()
        self.fields['glass'].initial = -1


# Форма экспорта продуктов
class CSVupload(forms.Form):
    csv_file = forms.FileField()
