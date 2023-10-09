from django.contrib.auth import get_user
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import UserFoodItem, ChooseDate, FoodItem
from .pagination import ProductsPagination, UserProductsPagination, WaterTrackerPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import FoodItemSerializer, UserFoodItemSerializerRead, UserFoodItemSerializerWrite, \
    WaterTrackerSerializer
from .utils import *
from rest_framework import generics, viewsets, mixins


# Представление дневника калорий
@login_required
def user_calc(request):
    # Определение актуального пользователя
    user = request.user
    cust = user.id

    # Меню выбора даты
    ch_date = ChooseDate.objects.filter(customer=cust)
    main_date = main_date_func(ch_date)

    # Счетчик стаканов воды
    water = WaterTracker.objects.filter(customer=user, drink_date=main_date)
    water_count = water_count_func(water)

    # Таблица завтрака
    breakfast = Category.objects.filter(name='breakfast')[0].userfooditem_set.all()
    my_breakfast = breakfast.filter(customer=cust, add_date=main_date)
    bcnt = my_breakfast.count()
    breakfast_list, breakfast_quantity_list, breakfast_list_id = food_list_prepare(my_breakfast)
    breakfast_view_list = ready_eating_list_func(eating_list_func(breakfast_list), breakfast_quantity_list)
    breakfast_view_dict = food_view_dict(breakfast_view_list, breakfast_list_id)
    calorie_count_br, protein_count_br, fats_count_br, carbohydrate_count_br, quantity_count_br = food_count(breakfast_view_list)

    # Таблица обеда
    lunch = Category.objects.filter(name='lunch')[0].userfooditem_set.all()
    my_lunch = lunch.filter(customer=cust, add_date=main_date)
    lcnt = my_lunch.count()
    lunch_list, lunch_quantity_list, lunch_list_id = food_list_prepare(my_lunch)
    lunch_view_list = ready_eating_list_func(eating_list_func(lunch_list), lunch_quantity_list)
    lunch_view_dict = food_view_dict(lunch_view_list, lunch_list_id)
    calorie_count_lu, protein_count_lu, fats_count_lu, carbohydrate_count_lu, quantity_count_lu = food_count(lunch_view_list)

    # Таблица ужина
    dinner = Category.objects.filter(name='dinner')[0].userfooditem_set.all()
    my_dinner = dinner.filter(customer=cust, add_date=main_date)
    dcnt = my_dinner.count()
    dinner_list, dinner_quantity_list, dinner_list_id = food_list_prepare(my_dinner)
    dinner_view_list = ready_eating_list_func(eating_list_func(dinner_list), dinner_quantity_list)
    dinner_view_dict = food_view_dict(dinner_view_list, dinner_list_id)
    calorie_count_di, protein_count_di, fats_count_di, carbohydrate_count_di, quantity_count_di = food_count(dinner_view_list)

    # Таблица перекусов
    snacks = Category.objects.filter(name='snacks')[0].userfooditem_set.all()
    my_snacks = snacks.filter(customer=cust, add_date=main_date)
    scnt = my_snacks.count()
    snacks_list, snacks_quantity_list, snacks_list_id = food_list_prepare(my_snacks)
    snacks_view_list = ready_eating_list_func(eating_list_func(snacks_list), snacks_quantity_list)
    snacks_view_dict = food_view_dict(snacks_view_list, snacks_list_id)
    calorie_count_sn, protein_count_sn, fats_count_sn, carbohydrate_count_sn, quantity_count_sn = food_count(snacks_view_list)

    # Итоговые значения
    calorie_count_all = calorie_count_br + calorie_count_lu + calorie_count_di + calorie_count_sn
    protein_count_all = protein_count_br + protein_count_lu + protein_count_di + protein_count_sn
    fats_count_all = fats_count_br + fats_count_lu + fats_count_di + fats_count_sn
    carbohydrate_count_all = carbohydrate_count_br + carbohydrate_count_lu + carbohydrate_count_di + carbohydrate_count_sn
    quantity_count_all = quantity_count_br + quantity_count_lu + quantity_count_di + quantity_count_sn

    if request.method == 'POST':
        # Форма трекера воды
        form_drink = WaterTrackerForm(request.POST, initial={'customer': user})
        if form_drink.is_valid():
            form_drink.save()
            return redirect('user_calc')

        # Форма создания пользовательской еды
        create_food_item_form = FoodItemForm(request.POST)
        if create_food_item_form.is_valid():
            create_food_item_form.save()
            return redirect('/calories_calc/user_calc/')

        # Форма добавления еды к завтраку
        form_br = AddUserFoodItemBreakfast(request.POST, initial={'customer': user})
        if form_br.is_valid():
            form_br.save()
            return redirect('/calories_calc/user_calc/')

        # Форма добавления еды к обеду
        form_lu = AddUserFoodItemLunch(request.POST, initial={'customer': user})
        if form_lu.is_valid():
            form_lu.save()
            return redirect('/calories_calc/user_calc/')

        # Форма добавления еды к ужину
        form_di = AddUserFoodItemDinner(request.POST, initial={'customer': user})
        if form_di.is_valid():
            form_di.save()
            return redirect('/calories_calc/user_calc/')

        # Форма добавления еды к перекусам
        form_sn = AddUserFoodItemSnacks(request.POST, initial={'customer': user})
        if form_sn.is_valid():
            form_sn.save()
            return redirect('/calories_calc/user_calc/')

        # Форма выбора даты
        form_ch = ChooseDateForm(request.POST, initial={'customer': user})
        if form_ch.is_valid():
            form_ch.save()
            return redirect('/calories_calc/user_calc/')

    form_drink = WaterTrackerForm(initial={'customer': user, 'drink_date': main_date})
    create_food_item_form = FoodItemForm(request.POST)
    form_br = AddUserFoodItemBreakfast(initial={'customer': user, 'add_date': main_date})
    form_lu = AddUserFoodItemLunch(initial={'customer': user, 'add_date': main_date})
    form_di = AddUserFoodItemDinner(initial={'customer': user, 'add_date': main_date})
    form_sn = AddUserFoodItemSnacks(initial={'customer': user, 'add_date': main_date})
    form_ch = ChooseDateForm(initial={'customer': user})

    context = {
        'main_date': main_date, 'create_food_item_form': create_food_item_form,

        'breakfast_view_dict': breakfast_view_dict, 'bcnt': bcnt,
        'lunch': lunch_view_list, 'lunch_view_dict': lunch_view_dict, 'lcnt': lcnt,
        'dinner': dinner_view_list, 'dinner_view_dict': dinner_view_dict, 'dcnt': dcnt,
        'snacks': snacks_view_list, 'snacks_view_dict': snacks_view_dict, 'scnt': scnt,

        'form_br': form_br, 'form_lu': form_lu, 'form_di': form_di, 'form_sn': form_sn, 'form_ch': form_ch,
        'form_drink': form_drink, 'water_count': water_count,

        'calorie_count_sn': calorie_count_sn,
        'protein_count_sn': protein_count_sn,
        'fats_count_sn': fats_count_sn,
        'carbohydrate_count_sn': carbohydrate_count_sn,
        'quantity_count_sn': quantity_count_sn,

        'calorie_count_br': calorie_count_br,
        'protein_count_br': protein_count_br,
        'fats_count_br': fats_count_br,
        'carbohydrate_count_br': carbohydrate_count_br,
        'quantity_count_br': quantity_count_br,

        'calorie_count_lu': calorie_count_lu,
        'protein_count_lu': protein_count_lu,
        'fats_count_lu': fats_count_lu,
        'carbohydrate_count_lu': carbohydrate_count_lu,
        'quantity_count_lu': quantity_count_lu,

        'calorie_count_di': calorie_count_di,
        'protein_count_di': protein_count_di,
        'fats_count_di': fats_count_di,
        'carbohydrate_count_di': carbohydrate_count_di,
        'quantity_count_di': quantity_count_di,

        'calorie_count_all': calorie_count_all,
        'protein_count_all': protein_count_all,
        'fats_count_all': fats_count_all,
        'carbohydrate_count_all': carbohydrate_count_all,
        'quantity_count_all': quantity_count_all,
    }

    return render(request, 'user_calc.html', context)


# Представление статистики
@login_required
def charts(request):
    # Определение актуального пользователя
    user = request.user
    cust = user.id

    # Меню выбора даты
    ch_date = ChooseDate.objects.filter(customer=cust)
    main_date = main_date_func(ch_date)

    # Таблица завтрака
    breakfast = Category.objects.filter(name='breakfast')[0].userfooditem_set.all()
    my_breakfast = breakfast.filter(customer=cust, add_date=main_date)
    breakfast_list, breakfast_quantity_list = food_list_prepare(my_breakfast)[:2]
    breakfast_view_list = ready_eating_list_func(eating_list_func(breakfast_list), breakfast_quantity_list)
    calorie_count_br, protein_count_br, fats_count_br, carbohydrate_count_br = food_count(breakfast_view_list)[:4]

    # Таблица обеда
    lunch = Category.objects.filter(name='lunch')[0].userfooditem_set.all()
    my_lunch = lunch.filter(customer=cust, add_date=main_date)
    lunch_list, lunch_quantity_list = food_list_prepare(my_lunch)[:2]
    lunch_view_list = ready_eating_list_func(eating_list_func(lunch_list), lunch_quantity_list)
    calorie_count_lu, protein_count_lu, fats_count_lu, carbohydrate_count_lu = food_count(lunch_view_list)[:4]

    # Таблица ужина
    dinner = Category.objects.filter(name='dinner')[0].userfooditem_set.all()
    my_dinner = dinner.filter(customer=cust, add_date=main_date)
    dinner_list, dinner_quantity_list = food_list_prepare(my_dinner)[:2]
    dinner_view_list = ready_eating_list_func(eating_list_func(dinner_list), dinner_quantity_list)
    calorie_count_di, protein_count_di, fats_count_di, carbohydrate_count_di = food_count(dinner_view_list)[:4]

    # Таблица перекусов
    snacks = Category.objects.filter(name='snacks')[0].userfooditem_set.all()
    my_snacks = snacks.filter(customer=cust, add_date=main_date)
    snacks_list, snacks_quantity_list = food_list_prepare(my_snacks)[:2]
    snacks_view_list = ready_eating_list_func(eating_list_func(snacks_list), snacks_quantity_list)
    calorie_count_sn, protein_count_sn, fats_count_sn, carbohydrate_count_sn = food_count(snacks_view_list)[:4]

    # Диаграммы
    food_nutrients_labels = ['Белки', 'Жиры', 'Углеводы']
    data_breakfast = [float(protein_count_br), float(fats_count_br), float(carbohydrate_count_br)]
    data_lunch = [float(protein_count_lu), float(fats_count_lu), float(carbohydrate_count_lu)]
    data_dinner = [float(protein_count_di), float(fats_count_di), float(carbohydrate_count_di)]
    data_snacks = [float(protein_count_sn), float(fats_count_sn), float(carbohydrate_count_sn)]

    food_category_labels = ['Завтрак', 'Обед', 'Ужин', 'Перекусы']
    food_category_data = [float(calorie_count_br),
                          float(calorie_count_lu),
                          float(calorie_count_di),
                          float(calorie_count_sn)
                          ]

    # Итоговые значения
    calorie_count_all = calorie_count_br + calorie_count_lu + calorie_count_di + calorie_count_sn

    if user.calories > 0:
        calorieleft = user.calories - calorie_count_all
    else:
        calorieleft = user.calories_per_day() - calorie_count_all

    total = UserFoodItem.objects.all()
    myfooditems = total.filter(customer=cust, add_date=main_date)
    cnt = myfooditems.count()

    # Счетчик стаканов воды
    water = WaterTracker.objects.filter(customer=user, drink_date=main_date)
    water_count = water_count_func(water)

    # Форма выбора даты
    if request.method == 'POST':
        form_ch = ChooseDateForm(request.POST, initial={'customer': user})
        if form_ch.is_valid():
            form_ch.save()
            return redirect('charts')
    form_ch = ChooseDateForm(initial={'customer': user})

    context = {
        'food_nutrients_labels': food_nutrients_labels, 'food_category_labels': food_category_labels,
        'food_category_data': food_category_data,
        'data_breakfast': data_breakfast,
        'data_lunch': data_lunch,
        'data_dinner': data_dinner,
        'data_snacks': data_snacks,
        'main_date': main_date,
        'form_ch': form_ch,
        'cnt': cnt,
        'water_count': water_count,
        'calorie_count_all': calorie_count_all, 'calorieleft': calorieleft,
    }

    return render(request, 'home.html', context)


# Удаление еды из списка
@login_required
def delete_food_item(request, item_id):
    item = get_object_or_404(UserFoodItem, id=item_id)
    item.delete()
    return redirect('/calories_calc/user_calc/')


# Загрузка CSV файла
@staff_member_required
def upload_csv(request):
    if request.method == 'POST':
        form = CSVupload(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            imported_products = import_products_from_csv(csv_file)
            request.session['imported_products'] = imported_products
            return redirect('show_imported_products')
    else:
        form = CSVupload()
    return render(request, 'upload_csv.html', {'form': form})


# Отображение импортированных продуктов
@staff_member_required
def show_imported_products(request):
    imported_products = request.session.get('imported_products', [])
    return render(request, 'imported_products.html', {'imported_products': imported_products})


# Вьюсет для работы с базой данных продуктов
class ProductsAPIViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = (IsAdminUser, )
    pagination_class = ProductsPagination



# Вьюсет для чтения пользовательских продуктами
class UserProductsAPIViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserFoodItemSerializerRead
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = UserProductsPagination

    def get_queryset(self):
        user = self.request.user.id
        return UserFoodItem.objects.filter(customer=user).values(
                                                'id',
                                                'customer__username',
                                                'fooditem__name',
                                                'category__name',
                                                'add_date',
                                                'quantity'
                                                )

    @action(detail=False, methods=['get'], url_path=r'(?P<dates>[0-9]{4}-?[0-9]{2}-?[0-9]{2})')
    def date_sort(self, request, dates):
        user = self.request.user.id
        today_list = UserFoodItem.objects.filter(customer=user, add_date=dates).values(
                                                'id',
                                                'customer__username',
                                                'fooditem__name',
                                                'category__name',
                                                'add_date',
                                                'quantity'
                                                )

        page = self.paginate_queryset(today_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(today_list, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'(?P<dates>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/breakfast')
    def breakfast(self, request, dates):
        user = self.request.user.id
        cat = Category.objects.filter(name='breakfast')[0]
        today_list = UserFoodItem.objects.filter(customer=user, category=cat, add_date=dates).values(
                                                'id',
                                                'customer__username',
                                                'fooditem__name',
                                                'category__name',
                                                'add_date',
                                                'quantity'
                                                )
        page = self.paginate_queryset(today_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(today_list, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'(?P<dates>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/lunch')
    def lunch(self, request, dates):
        user = self.request.user.id
        cat = Category.objects.filter(name='lunch')[0]
        today_list = UserFoodItem.objects.filter(customer=user, category=cat, add_date=dates).values(
                                                'id',
                                                'customer__username',
                                                'fooditem__name',
                                                'category__name',
                                                'add_date',
                                                'quantity'
                                                )
        page = self.paginate_queryset(today_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(today_list, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'(?P<dates>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/dinner')
    def dinner(self, request, dates):
        user = self.request.user.id
        cat = Category.objects.filter(name='dinner')[0]
        today_list = UserFoodItem.objects.filter(customer=user, category=cat, add_date=dates).values(
                                                'id',
                                                'customer__username',
                                                'fooditem__name',
                                                'category__name',
                                                'add_date',
                                                'quantity'
                                                )
        page = self.paginate_queryset(today_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(today_list, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'(?P<dates>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/snacks')
    def snacks(self, request, dates):
        user = self.request.user.id
        cat = Category.objects.filter(name='snacks')[0]
        today_list = UserFoodItem.objects.filter(customer=user, category=cat, add_date=dates).values(
                                                                                                'id',
                                                                                                'customer__username',
                                                                                                'fooditem__name',
                                                                                                'category__name',
                                                                                                'add_date',
                                                                                                'quantity'
                                                                                                )
        page = self.paginate_queryset(today_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(today_list, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'(?P<dates>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/statistics')
    def statistics(self, request, dates):
        user = self.request.user.id
        today_list = UserFoodItem.objects.filter(customer=user, add_date=dates)

        product_counter = len(today_list)
        norm_calories = [i.get('calories') for i in CustomUser.objects.filter(id=user).values('calories')][0]
        if norm_calories == 0:
            norm_calories = CustomUser.calories_per_day(CustomUser.objects.get(id=user))

        quantity = [i.get('quantity') for i in today_list.values('quantity')]
        fooditem_calories = [i.get('fooditem__calorie') / 100 for i in UserFoodItem.objects.filter(customer=user, add_date=dates).values('fooditem__calorie')]
        calories_counter = []
        for k in range(len(quantity)):
            cal = quantity[k] * fooditem_calories[k]
            calories_counter.append(cal)
        calories_counter = round(sum(calories_counter), 2)

        remaining_calories_counter = norm_calories - calories_counter

        fooditem_protein = [i.get('fooditem__protein') / 100 for i in UserFoodItem.objects.filter(customer=user, add_date=dates).values('fooditem__protein')]
        protein_counter = []
        for k in range(len(quantity)):
            prot = quantity[k] * fooditem_protein[k]
            protein_counter.append(prot)
        protein_counter = round(sum(protein_counter), 2)

        fooditem_fats = [i.get('fooditem__fats') / 100 for i in
                            UserFoodItem.objects.filter(customer=user, add_date=dates).values('fooditem__fats')]
        fats_counter = []
        for k in range(len(quantity)):
            fats = quantity[k] * fooditem_fats[k]
            fats_counter.append(fats)
        fats_counter = round(sum(fats_counter), 2)

        fooditem_carb = [i.get('fooditem__carbohydrate') / 100 for i in
                         UserFoodItem.objects.filter(customer=user, add_date=dates).values('fooditem__carbohydrate')]
        carb_counter = []
        for k in range(len(quantity)):
            carb = quantity[k] * fooditem_carb[k]
            carb_counter.append(carb)
        carb_counter = round(sum(carb_counter), 2)

        context = {
            'all_products': product_counter,
            'norm_calories': norm_calories,
            'calories_counter': calories_counter,
            'remaining_calories_counter': remaining_calories_counter,
            'protein_counter': protein_counter,
            'fats_counter': fats_counter,
            'carb_counter': carb_counter,
        }
        return Response(context)


# Вьюсет для редактирования пользовательских продуктами
class UserProductsAPIViewSetWrite(viewsets.ModelViewSet):
    serializer_class = UserFoodItemSerializerWrite
    permission_classes = (IsOwnerOrReadOnly, )
    pagination_class = UserProductsPagination

    def get_queryset(self):
        user = self.request.user.id
        return UserFoodItem.objects.filter(customer=user)


# Вьюсет для трекера воды (когда будет добавлена регистрация - отредактировать)
class WaterTrackerAPIViewSet(viewsets.ModelViewSet):
    serializer_class = WaterTrackerSerializer
    pagination_class = WaterTrackerPagination

    def get_queryset(self):
        user = self.request.user.id
        return WaterTracker.objects.filter(customer=user)

    @action(detail=False, methods=['get'], url_path=r'(?P<dates>[0-9]{4}-?[0-9]{2}-?[0-9]{2})')
    def all_glasses(self, request, dates):
        user = self.request.user.id
        water_tracker_list = WaterTracker.objects.filter(customer=user, drink_date=dates)
        glass_counter = 0
        for i in water_tracker_list.values('glass'):
            glass_counter += i.get('glass')
        return Response({'all_glasses': glass_counter})
