from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import UserFoodItem, ChooseDate
from .utils import *


# Представление дневника калорий
@login_required
def user_calc(request):
    user = request.user
    cust = user.id

    ch_date = ChooseDate.objects.filter(customer=cust)
    main_date = main_date_func(ch_date)

    water = WaterTracker.objects.filter(customer=user, drink_date=main_date)
    water_count = water_count_func(water)

    breakfast = Category.objects.filter(name='breakfast')[0].userfooditem_set.all()
    my_breakfast = breakfast.filter(customer=cust, add_date=main_date)
    bcnt = my_breakfast.count()

    breakfast_list = food_list_prepare(my_breakfast)[0]
    breakfast_list_id = food_list_prepare(my_breakfast)[1]
    breakfast_quantity_list = food_list_prepare(my_breakfast)[2]

    breakfast_view_list = eatinglist(breakfast_list)
    breakfast_view_list = eating(breakfast_view_list, breakfast_quantity_list)

    breakfast_view_dict = food_view_dict(breakfast_view_list, breakfast_list_id)

    calorie_count_br = food_count(breakfast_view_list)[0]
    protein_count_br = food_count(breakfast_view_list)[1]
    fats_count_br = food_count(breakfast_view_list)[2]
    carbohydrate_count_br = food_count(breakfast_view_list)[3]
    quantity_count_br = food_count(breakfast_view_list)[4]

    lunch = Category.objects.filter(name='lunch')[0].userfooditem_set.all()
    my_lunch = lunch.filter(customer=cust, add_date=main_date)
    lcnt = my_lunch.count()

    lunch_list = food_list_prepare(my_lunch)[0]
    lunch_list_id = food_list_prepare(my_lunch)[1]
    lunch_quantity_list = food_list_prepare(my_lunch)[2]

    lunch_view_list = eatinglist(lunch_list)
    lunch_view_list = eating(lunch_view_list, lunch_quantity_list)

    lunch_view_dict = food_view_dict(lunch_view_list, lunch_list_id)

    calorie_count_lu = food_count(lunch_view_list)[0]
    protein_count_lu = food_count(lunch_view_list)[1]
    fats_count_lu = food_count(lunch_view_list)[2]
    carbohydrate_count_lu = food_count(lunch_view_list)[3]
    quantity_count_lu = food_count(lunch_view_list)[4]

    dinner = Category.objects.filter(name='dinner')[0].userfooditem_set.all()
    my_dinner = dinner.filter(customer=cust, add_date=main_date)
    dcnt = my_dinner.count()

    dinner_list = food_list_prepare(my_dinner)[0]
    dinner_list_id = food_list_prepare(my_dinner)[1]
    dinner_quantity_list = food_list_prepare(my_dinner)[2]

    dinner_view_list = eatinglist(dinner_list)
    dinner_view_list = eating(dinner_view_list, dinner_quantity_list)

    dinner_view_dict = food_view_dict(dinner_view_list, dinner_list_id)

    calorie_count_di = food_count(dinner_view_list)[0]
    protein_count_di = food_count(dinner_view_list)[1]
    fats_count_di = food_count(dinner_view_list)[2]
    carbohydrate_count_di = food_count(dinner_view_list)[3]
    quantity_count_di = food_count(dinner_view_list)[4]

    snacks = Category.objects.filter(name='snacks')[0].userfooditem_set.all()
    my_snacks = snacks.filter(customer=cust, add_date=main_date)
    scnt = my_snacks.count()
    snacks_list = food_list_prepare(my_snacks)[0]
    snacks_list_id = food_list_prepare(my_snacks)[1]
    snacks_quantity_list = food_list_prepare(my_snacks)[2]

    snacks_view_list = eatinglist(snacks_list)
    snacks_view_list = eating(snacks_view_list, snacks_quantity_list)

    snacks_view_dict = food_view_dict(snacks_view_list, snacks_list_id)

    calorie_count_sn = food_count(snacks_view_list)[0]
    protein_count_sn = food_count(snacks_view_list)[1]
    fats_count_sn = food_count(snacks_view_list)[2]
    carbohydrate_count_sn = food_count(snacks_view_list)[3]
    quantity_count_sn = food_count(snacks_view_list)[4]

    calorie_count_all = calorie_count_br + calorie_count_lu + calorie_count_di + calorie_count_sn
    protein_count_all = protein_count_br + protein_count_lu + protein_count_di + protein_count_sn
    fats_count_all = fats_count_br + fats_count_lu + fats_count_di + fats_count_sn
    carbohydrate_count_all = carbohydrate_count_br + carbohydrate_count_lu + carbohydrate_count_di + carbohydrate_count_sn
    quantity_count_all = quantity_count_br + quantity_count_lu + quantity_count_di + quantity_count_sn

    if request.method == 'POST':
        form_drink = WaterTrackerForm(request.POST, initial={'customer': user})
        if form_drink.is_valid():
            form_drink.save()
            return redirect('user_calc')

        create_food_item_form = FoodItemForm(request.POST)
        if create_food_item_form.is_valid():
            create_food_item_form.save()
            return redirect('/calories_calc/user_calc/')

        form_br = AddUserFoodItemBreakfast(request.POST, initial={'customer': user})
        if form_br.is_valid():
            form_br.save()
            return redirect('/calories_calc/user_calc/')

        form_lu = AddUserFoodItemLunch(request.POST, initial={'customer': user})
        if form_lu.is_valid():
            form_lu.save()
            return redirect('/calories_calc/user_calc/')

        form_di = AddUserFoodItemDinner(request.POST, initial={'customer': user})
        if form_di.is_valid():
            form_di.save()
            return redirect('/calories_calc/user_calc/')

        form_sn = AddUserFoodItemSnacks(request.POST, initial={'customer': user})
        if form_sn.is_valid():
            form_sn.save()
            return redirect('/calories_calc/user_calc/')

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


# Представление статистики
@login_required
def charts(request):
    user = request.user
    cust = user.id

    ch_date = ChooseDate.objects.filter(customer=cust)
    main_date = main_date_func(ch_date)

    breakfast = Category.objects.filter(name='breakfast')[0].userfooditem_set.all()
    my_breakfast = breakfast.filter(customer=cust, add_date=main_date)

    breakfast_list = food_list_prepare(my_breakfast)[0]
    breakfast_quantity_list = food_list_prepare(my_breakfast)[2]

    breakfast_view_list = eatinglist(breakfast_list)
    breakfast_view_list = eating(breakfast_view_list, breakfast_quantity_list)

    calorie_count_br = food_count(breakfast_view_list)[0]
    protein_count_br = food_count(breakfast_view_list)[1]
    fats_count_br = food_count(breakfast_view_list)[2]
    carbohydrate_count_br = food_count(breakfast_view_list)[3]

    lunch = Category.objects.filter(name='lunch')[0].userfooditem_set.all()
    my_lunch = lunch.filter(customer=cust, add_date=main_date)
    lunch_list = food_list_prepare(my_lunch)[0]
    lunch_quantity_list = food_list_prepare(my_lunch)[2]

    lunch_view_list = eatinglist(lunch_list)
    lunch_view_list = eating(lunch_view_list, lunch_quantity_list)

    calorie_count_lu = food_count(lunch_view_list)[0]
    protein_count_lu = food_count(lunch_view_list)[1]
    fats_count_lu = food_count(lunch_view_list)[2]
    carbohydrate_count_lu = food_count(lunch_view_list)[3]

    dinner = Category.objects.filter(name='dinner')[0].userfooditem_set.all()
    my_dinner = dinner.filter(customer=cust, add_date=main_date)
    dinner_list = food_list_prepare(my_dinner)[0]
    dinner_quantity_list = food_list_prepare(my_dinner)[2]

    dinner_view_list = eatinglist(dinner_list)
    dinner_view_list = eating(dinner_view_list, dinner_quantity_list)

    calorie_count_di = food_count(dinner_view_list)[0]
    protein_count_di = food_count(dinner_view_list)[1]
    fats_count_di = food_count(dinner_view_list)[2]
    carbohydrate_count_di = food_count(dinner_view_list)[3]

    snacks = Category.objects.filter(name='snacks')[0].userfooditem_set.all()
    my_snacks = snacks.filter(customer=cust, add_date=main_date)
    snacks_list = food_list_prepare(my_snacks)[0]
    snacks_quantity_list = food_list_prepare(my_snacks)[2]

    snacks_view_list = eatinglist(snacks_list)
    snacks_view_list = eating(snacks_view_list, snacks_quantity_list)

    calorie_count_sn = food_count(snacks_view_list)[0]
    protein_count_sn = food_count(snacks_view_list)[1]
    fats_count_sn = food_count(snacks_view_list)[2]
    carbohydrate_count_sn = food_count(snacks_view_list)[3]

    food_nutrients_labels = ['Белки', 'Жиры', 'Углеводы']
    data_breakfast = [float(protein_count_br), float(fats_count_br), float(carbohydrate_count_br)]
    data_lunch = [float(protein_count_lu), float(fats_count_lu), float(carbohydrate_count_lu)]
    data_dinner = [float(protein_count_di), float(fats_count_di), float(carbohydrate_count_di)]
    data_snacks = [float(protein_count_sn), float(fats_count_sn), float(carbohydrate_count_sn)]

    food_category_labels = ['Завтрак', 'Обед', 'Ужин', 'Перекусы']
    food_category_data = [float(calorie_count_br), float(calorie_count_lu), float(calorie_count_di),
                          float(calorie_count_sn)]

    calorie_count_all = calorie_count_br + calorie_count_lu + calorie_count_di + calorie_count_sn

    if user.calories > 0:
        calorieleft = user.calories - calorie_count_all
    else:
        calorieleft = user.calories_per_day() - calorie_count_all

    total = UserFoodItem.objects.all()
    myfooditems = total.filter(customer=cust, add_date=main_date)
    cnt = myfooditems.count()

    water = WaterTracker.objects.filter(customer=user, drink_date=main_date)
    water_count = water_count_func(water)

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
