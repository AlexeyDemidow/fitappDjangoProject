# Generated by Django 4.2.3 on 2023-07-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories_calc', '0006_remove_fooditem_category_userfooditem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='category',
            field=models.ManyToManyField(to='calories_calc.category'),
        ),
    ]
