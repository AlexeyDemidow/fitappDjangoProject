# Generated by Django 4.2.3 on 2023-08-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_activity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='calories',
            field=models.IntegerField(default=0, verbose_name='Количество калорий в день'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='weight',
            field=models.FloatField(default=0, help_text='Введите в килограммах', verbose_name='Вес'),
        ),
    ]
