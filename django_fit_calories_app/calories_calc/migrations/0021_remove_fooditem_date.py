# Generated by Django 4.2.3 on 2023-09-03 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calories_calc', '0020_fooditem_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='date',
        ),
    ]
