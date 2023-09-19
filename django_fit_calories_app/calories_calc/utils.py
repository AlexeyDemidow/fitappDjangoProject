import csv
from .models import FoodItem
from decimal import Decimal
from datetime import date


# Выбранная дата
def main_date_func(dates):
    ch_dt_list = [date.today()]
    for dt in dates:
        ch_dt_list.clear()
        ch_dt_list.append(dt.c_date)
    main_date = ch_dt_list[0]
    return main_date


# Счетчик стаканов воды
def water_count_func(glasses):
    water_count = 0
    for water_glass in glasses:
        water_count += water_glass.glass
    return water_count


# Обработка запроса и распределение данных по спискам
def food_list_prepare(my_food):
    food_list = []
    food_list_id = []
    food_quantity_list = []
    for item in my_food:
        food_list.append(item.fooditem.all())
        food_quantity_list.append(item.quantity)
        food_list_id.append(item.id)
    return food_list, food_quantity_list, food_list_id


# Преобразование запросов в данные
def eating_list_func(eat_list):
    eating_view_list = []
    for items in eat_list:
        for food in items:
            eating_view_list.append(food)
    return eating_view_list


# Подсчет количества нутриентов в зависимости от массы
def ready_eating_list_func(eat_list, quantity_list):
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


# Создание словаря название еды: характеристики
def food_view_dict(food_view_list, food_list_id):
    food_view_dictionary = {}
    for d_index in range(len(food_view_list)):
        food_view_dictionary[food_list_id[d_index]] = food_view_list[d_index]
    return food_view_dictionary


# Подсчет количества нутриентов
def food_count(food_view_list):
    calorie_count = 0
    protein_count = 0
    fats_count = 0
    carbohydrate_count = 0
    quantity_count = 0
    for j in range(len(food_view_list)):
        calorie_count += food_view_list[j].calorie
        protein_count += food_view_list[j].protein
        fats_count += food_view_list[j].fats
        carbohydrate_count += food_view_list[j].carbohydrate
        quantity_count += food_view_list[j].quantity
    return calorie_count, protein_count, fats_count, carbohydrate_count, quantity_count


# Импорт еды из CSV-файла
def import_products_from_csv(csv_file):
    reader = csv.DictReader(csv_file.read().decode('utf-8').splitlines(), delimiter=';')
    for row in reader:
        product = FoodItem(
            name=row['name'],
            protein=float(row['protein'].replace('%', '')),
            fats=float(row['fats'].replace('%', '')),
            carbohydrate=float(row['carbohydrate'].replace('%', '')),
            calorie=float(row['calorie'].replace('%', '')),
        )
        product.save()

