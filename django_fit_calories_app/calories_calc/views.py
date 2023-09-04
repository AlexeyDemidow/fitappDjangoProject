from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import UserFoodItem, ChooseDate
from .utils import import_products_from_csv
from decimal import Decimal
from datetime import date


# Подсчет количества нутриентов в зависимости от массы
def eating(eat_list, quantity_list):
    if len(eat_list) > 0:
        for i in range(len(quantity_list)):
            eat_list[i].calorie *= Decimal(quantity_list[i]) / 100
            eat_list[i].calorie = eat_list[i].calorie.quantize(Decimal("1.00"))

            eat_list[i].protein *= Decimal(quantity_list[i]) / 100
            eat_list[i].protein = eat_list[i].protein.quantize(Decimal("1.00"))

            eat_list[i].fats *= Decimal(quantity_list[i]) / 100
            eat_list[i].fats = eat_list[i].fats.quantize(Decimal("1.00"))

            eat_list[i].carbohydrate *= Decimal(quantity_list[i]) / 100
            eat_list[i].carbohydrate = eat_list[i].carbohydrate.quantize(Decimal("1.00"))

            eat_list[i].quantity *= Decimal(quantity_list[i]) / 100
            eat_list[i].quantity = eat_list[i].quantity.quantize(Decimal("1.00"))
    return eat_list


def eatinglist(eat_list):
    eating_view_list = []
    for items in eat_list:
        for food in items:
            eating_view_list.append(food)
    return eating_view_list


# Представление дневника калорий
@login_required
def user_calc(request):
    user = request.user
    cust = user.id

    ch_date = ChooseDate.objects.filter(customer=cust)
    ch_dt_list = [date.today()]
    for dt in ch_date:
        ch_dt_list.clear()
        ch_dt_list.append(dt.c_date)
    main_date = ch_dt_list[0]

    if request.method == 'POST':
        form_drink = WaterTrackerForm(request.POST, initial={'customer': user})
        if form_drink.is_valid():
            form_drink.save()
            return redirect('user_calc')
    form_drink = WaterTrackerForm(initial={'customer': user, 'drink_date': main_date})

    water = WaterTracker.objects.filter(customer=user, drink_date=main_date)
    water_count = 0
    for water_glass in water:
        water_count += water_glass.glass

    if request.method == 'POST':
        create_food_item_form = FoodItemForm(request.POST)
        if create_food_item_form.is_valid():
            create_food_item_form.save()
            return redirect('/calories_calc/user_calc/')
    create_food_item_form = FoodItemForm(request.POST)

    breakfast = Category.objects.filter(name='breakfast')[0].userfooditem_set.all()
    my_breakfast = breakfast.filter(customer=cust, add_date=main_date)
    bcnt = my_breakfast.count()
    breakfast_list = []
    breakfast_list_id = []
    breakfast_quantity_list = []
    for item in my_breakfast:
        breakfast_list.append(item.fooditem.all())
        breakfast_list_id.append(item.id)
        breakfast_quantity_list.append(item.quantity)

    breakfast_view_list = eatinglist(breakfast_list)
    breakfast_view_list = eating(breakfast_view_list, breakfast_quantity_list)

    breakfast_view_dict = {}
    for d_index in range(len(breakfast_view_list)):
        breakfast_view_dict[breakfast_list_id[d_index]] = breakfast_view_list[d_index]

    calorie_count_br = 0
    protein_count_br = 0
    fats_count_br = 0
    carbohydrate_count_br = 0
    quantity_count_br = 0
    for j in range(len(breakfast_view_list)):
        calorie_count_br += breakfast_view_list[j].calorie
        protein_count_br += breakfast_view_list[j].protein
        fats_count_br += breakfast_view_list[j].fats
        carbohydrate_count_br += breakfast_view_list[j].carbohydrate
        quantity_count_br += breakfast_view_list[j].quantity

    lunch = Category.objects.filter(name='lunch')[0].userfooditem_set.all()
    my_lunch = lunch.filter(customer=cust, add_date=main_date)
    lcnt = my_lunch.count()
    lunch_list = []
    lunch_quantity_list = []
    lunch_list_id = []
    for item in my_lunch:
        lunch_list.append(item.fooditem.all())
        lunch_list_id.append(item.id)
        lunch_quantity_list.append(item.quantity)

    lunch_view_list = eatinglist(lunch_list)
    lunch_view_list = eating(lunch_view_list, lunch_quantity_list)

    lunch_view_dict = {}
    for d_index in range(len(lunch_view_list)):
        lunch_view_dict[lunch_list_id[d_index]] = lunch_view_list[d_index]

    calorie_count_lu = 0
    protein_count_lu = 0
    fats_count_lu = 0
    carbohydrate_count_lu = 0
    quantity_count_lu = 0
    for j in range(len(lunch_view_list)):
        calorie_count_lu += lunch_view_list[j].calorie
        protein_count_lu += lunch_view_list[j].protein
        fats_count_lu += lunch_view_list[j].fats
        carbohydrate_count_lu += lunch_view_list[j].carbohydrate
        quantity_count_lu += lunch_view_list[j].quantity

    dinner = Category.objects.filter(name='dinner')[0].userfooditem_set.all()
    my_dinner = dinner.filter(customer=cust, add_date=main_date)
    dcnt = my_dinner.count()
    dinner_list = []
    dinner_list_id = []
    dinner_quantity_list = []
    for item in my_dinner:
        dinner_list.append(item.fooditem.all())
        dinner_list_id.append(item.id)
        dinner_quantity_list.append(item.quantity)

    dinner_view_list = eatinglist(dinner_list)
    dinner_view_list = eating(dinner_view_list, dinner_quantity_list)

    dinner_view_dict = {}
    for d_index in range(len(dinner_view_list)):
        dinner_view_dict[dinner_list_id[d_index]] = dinner_view_list[d_index]

    calorie_count_di = 0
    protein_count_di = 0
    fats_count_di = 0
    carbohydrate_count_di = 0
    quantity_count_di = 0
    for j in range(len(dinner_view_list)):
        calorie_count_di += dinner_view_list[j].calorie
        protein_count_di += dinner_view_list[j].protein
        fats_count_di += dinner_view_list[j].fats
        carbohydrate_count_di += dinner_view_list[j].carbohydrate
        quantity_count_di += dinner_view_list[j].quantity

    snacks = Category.objects.filter(name='snacks')[0].userfooditem_set.all()
    my_snacks = snacks.filter(customer=cust, add_date=main_date)
    scnt = my_snacks.count()
    snacks_list = []
    snacks_list_id = []
    snacks_quantity_list = []
    for item in my_snacks:
        snacks_list.append(item.fooditem.all())
        snacks_list_id.append(item.id)
        snacks_quantity_list.append(item.quantity)

    snacks_view_list = eatinglist(snacks_list)
    snacks_view_list = eating(snacks_view_list, snacks_quantity_list)

    snacks_view_dict = {}
    for d_index in range(len(snacks_view_list)):
        snacks_view_dict[snacks_list_id[d_index]] = snacks_view_list[d_index]

    calorie_count_sn = 0
    protein_count_sn = 0
    fats_count_sn = 0
    carbohydrate_count_sn = 0
    quantity_count_sn = 0
    for j in range(len(snacks_view_list)):
        calorie_count_sn += snacks_view_list[j].calorie
        protein_count_sn += snacks_view_list[j].protein
        fats_count_sn += snacks_view_list[j].fats
        carbohydrate_count_sn += snacks_view_list[j].carbohydrate
        quantity_count_sn += snacks_view_list[j].quantity

    calorie_count_all = calorie_count_br + calorie_count_lu + calorie_count_di + calorie_count_sn
    protein_count_all = protein_count_br + protein_count_lu + protein_count_di + protein_count_sn
    fats_count_all = fats_count_br + fats_count_lu + fats_count_di + fats_count_sn
    carbohydrate_count_all = carbohydrate_count_br + carbohydrate_count_lu + carbohydrate_count_di + carbohydrate_count_sn
    quantity_count_all = quantity_count_br + quantity_count_lu + quantity_count_di + quantity_count_sn

    if request.method == "POST":
        form_br = AddUserFoodItemBreakfast(request.POST, initial={'customer': user})
        if form_br.is_valid():
            form_br.save()
            return redirect('/calories_calc/user_calc/')
    form_br = AddUserFoodItemBreakfast(initial={'customer': user, 'add_date': main_date})

    if request.method == "POST":
        form_lu = AddUserFoodItemLunch(request.POST, initial={'customer': user})
        if form_lu.is_valid():
            form_lu.save()
            return redirect('/calories_calc/user_calc/')
    form_lu = AddUserFoodItemLunch(initial={'customer': user, 'add_date': main_date})

    if request.method == "POST":
        form_di = AddUserFoodItemDinner(request.POST, initial={'customer': user})
        if form_di.is_valid():
            form_di.save()
            return redirect('/calories_calc/user_calc/')
    form_di = AddUserFoodItemDinner(initial={'customer': user, 'add_date': main_date})

    if request.method == "POST":
        form_sn = AddUserFoodItemSnacks(request.POST, initial={'customer': user})
        if form_sn.is_valid():
            form_sn.save()
            return redirect('/calories_calc/user_calc/')
    form_sn = AddUserFoodItemSnacks(initial={'customer': user, 'add_date': main_date})

    if request.method == 'POST':
        form_ch = ChooseDateForm(request.POST, initial={'customer': user})
        if form_ch.is_valid():
            form_ch.save()
            return redirect('/calories_calc/user_calc/')
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
def deletefooditem(request, item_id):
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
    ch_dt_list = [date.today()]
    for dt in ch_date:
        ch_dt_list.clear()
        ch_dt_list.append(dt.c_date)
    main_date = ch_dt_list[0]

    breakfast = Category.objects.filter(name='breakfast')[0].userfooditem_set.all()
    my_breakfast = breakfast.filter(customer=cust, add_date=main_date)
    breakfast_list = []
    breakfast_quantity_list = []
    for item in my_breakfast:
        breakfast_list.append(item.fooditem.all())
        breakfast_quantity_list.append(item.quantity)

    breakfast_view_list = eatinglist(breakfast_list)
    breakfast_view_list = eating(breakfast_view_list, breakfast_quantity_list)

    calorie_count_br = 0
    protein_count_br = 0
    fats_count_br = 0
    carbohydrate_count_br = 0
    for j in range(len(breakfast_view_list)):
        calorie_count_br += breakfast_view_list[j].calorie
        protein_count_br += breakfast_view_list[j].protein
        fats_count_br += breakfast_view_list[j].fats
        carbohydrate_count_br += breakfast_view_list[j].carbohydrate

    lunch = Category.objects.filter(name='lunch')[0].userfooditem_set.all()
    my_lunch = lunch.filter(customer=cust, add_date=main_date)
    lunch_list = []
    lunch_quantity_list = []
    for item in my_lunch:
        lunch_list.append(item.fooditem.all())
        lunch_quantity_list.append(item.quantity)

    lunch_view_list = eatinglist(lunch_list)
    lunch_view_list = eating(lunch_view_list, lunch_quantity_list)

    calorie_count_lu = 0
    protein_count_lu = 0
    fats_count_lu = 0
    carbohydrate_count_lu = 0
    for j in range(len(lunch_view_list)):
        calorie_count_lu += lunch_view_list[j].calorie
        protein_count_lu += lunch_view_list[j].protein
        fats_count_lu += lunch_view_list[j].fats
        carbohydrate_count_lu += lunch_view_list[j].carbohydrate

    dinner = Category.objects.filter(name='dinner')[0].userfooditem_set.all()
    my_dinner = dinner.filter(customer=cust, add_date=main_date)
    dinner_list = []
    dinner_quantity_list = []
    for item in my_dinner:
        dinner_list.append(item.fooditem.all())
        dinner_quantity_list.append(item.quantity)

    dinner_view_list = eatinglist(dinner_list)
    dinner_view_list = eating(dinner_view_list, dinner_quantity_list)

    calorie_count_di = 0
    protein_count_di = 0
    fats_count_di = 0
    carbohydrate_count_di = 0
    for j in range(len(dinner_view_list)):
        calorie_count_di += dinner_view_list[j].calorie
        protein_count_di += dinner_view_list[j].protein
        fats_count_di += dinner_view_list[j].fats
        carbohydrate_count_di += dinner_view_list[j].carbohydrate

    snacks = Category.objects.filter(name='snacks')[0].userfooditem_set.all()
    my_snacks = snacks.filter(customer=cust, add_date=main_date)
    snacks_list = []
    snacks_quantity_list = []
    for item in my_snacks:
        snacks_list.append(item.fooditem.all())
        snacks_quantity_list.append(item.quantity)

    snacks_view_list = eatinglist(snacks_list)
    snacks_view_list = eating(snacks_view_list, snacks_quantity_list)

    calorie_count_sn = 0
    protein_count_sn = 0
    fats_count_sn = 0
    carbohydrate_count_sn = 0
    quantity_count_sn = 0
    for j in range(len(snacks_view_list)):
        calorie_count_sn += snacks_view_list[j].calorie
        protein_count_sn += snacks_view_list[j].protein
        fats_count_sn += snacks_view_list[j].fats
        carbohydrate_count_sn += snacks_view_list[j].carbohydrate
        quantity_count_sn += snacks_view_list[j].quantity

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

    if request.method == 'POST':
        form_ch = ChooseDateForm(request.POST, initial={'customer': user})
        if form_ch.is_valid():
            form_ch.save()
            return redirect('charts')
    form_ch = ChooseDateForm(initial={'customer': user})

    water = WaterTracker.objects.filter(customer=user, drink_date=main_date)
    water_count = 0
    for water_glass in water:
        water_count += water_glass.glass

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
