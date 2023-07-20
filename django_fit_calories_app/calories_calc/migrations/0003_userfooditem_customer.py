# Generated by Django 4.2.3 on 2023-07-18 14:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calories_calc', '0002_remove_userfooditem_customer_alter_fooditem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfooditem',
            name='customer',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
