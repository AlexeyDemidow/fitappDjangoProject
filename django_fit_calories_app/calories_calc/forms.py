from django.forms import ModelForm
from .models import *
from users.models import CustomUser
from datetime import datetime
from django import forms


class FoodItemForm(ModelForm):
    """Форма еды"""

    class Meta:
        model = FoodItem
        fields = ['name', 'calorie', 'protein', 'fats', 'carbohydrate', 'quantity']


class AddUserFoodItemBreakfast(ModelForm):
    """Форма добавления еды к завтраку"""

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    def __init__(self, *args, **kwargs):
        """Заполнение полей по умолчанию"""

        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='breakfast')
        self.fields['add_date'].initial = datetime.now().date()


class AddUserFoodItemLunch(ModelForm):
    """Форма добавления еды обеду"""

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='lunch')
        self.fields['add_date'].initial = datetime.now().date()


class AddUserFoodItemDinner(ModelForm):
    """Форма добавления еды ужину"""

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='dinner')
        self.fields['add_date'].initial = datetime.now().date()


class AddUserFoodItemSnacks(ModelForm):
    """Форма добавления еды перекусам"""

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='snacks')
        self.fields['add_date'].initial = datetime.now().date()


class ChooseDateForm(ModelForm):
    """Форма выбора даты"""

    class Meta:
        model = ChooseDate
        fields = ['c_date', 'customer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])


class WaterTrackerFormPlus(ModelForm):
    """Форма трекера воды, увеличение количества выпитой воды"""

    class Meta:
        model = WaterTracker
        fields = ['glass', 'drink_date', 'customer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['drink_date'].initial = datetime.now().date()
        self.fields['glass'].initial = 1


class WaterTrackerFormMinus(ModelForm):
    """Форма уменьшения количества выпитой воды"""
    class Meta:
        model = WaterTracker
        fields = ['glass', 'drink_date', 'customer']

    # Заполнение полей по умолчанию
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['drink_date'].initial = datetime.now().date()
        self.fields['glass'].initial = -1


class CSVupload(forms.Form):
    """Экспорт продуктов"""

    csv_file = forms.FileField()
