import csv
import os
from django.core.files.base import ContentFile
from django.core.files import File
from .models import FoodItem

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