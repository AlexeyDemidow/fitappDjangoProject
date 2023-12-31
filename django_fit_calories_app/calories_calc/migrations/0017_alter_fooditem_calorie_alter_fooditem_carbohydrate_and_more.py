# Generated by Django 4.2.3 on 2023-08-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories_calc', '0016_alter_fooditem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='calorie',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Калории'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='carbohydrate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Углеводы'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='fats',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Жиры'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='protein',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Белки'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='quantity',
            field=models.IntegerField(blank=True, default=100, null=True, verbose_name='Количество в граммах'),
        ),
    ]
