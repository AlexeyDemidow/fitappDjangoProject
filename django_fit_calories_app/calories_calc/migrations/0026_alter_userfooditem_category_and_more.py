# Generated by Django 4.2.3 on 2023-10-04 18:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calories_calc', '0025_remove_fooditem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfooditem',
            name='category',
            field=models.ManyToManyField(to='calories_calc.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='userfooditem',
            name='customer',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='userfooditem',
            name='fooditem',
            field=models.ManyToManyField(to='calories_calc.fooditem', verbose_name='Еда'),
        ),
    ]