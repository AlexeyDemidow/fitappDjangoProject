# Generated by Django 4.2.3 on 2023-07-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='activity',
            field=models.CharField(choices=[(1.2, 1.2), (1.375, 1.375), (1.55, 1.55), (1.7, 1.7), (1.9, 1.9)], default=1.2, max_length=10, verbose_name='Уровеь активности'),
        ),
    ]
