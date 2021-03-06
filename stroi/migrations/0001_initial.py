# Generated by Django 3.2 on 2021-04-23 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Чуйская', 'Чуйская'), ('Таласская', 'Таласская'), ('Баткенская', 'Баткенская'), ('Иссык-кульская', 'Иссык-кульская'), ('Нарынская', 'Нарынская'), ('Ошская', 'Ошская'), ('Джалал-Абадская', 'Джалал-Абадская')], max_length=20)),
                ('address', models.CharField(blank=True, max_length=30, verbose_name='Адрес объекта')),
                ('start_date', models.DateField(verbose_name='Дата начала стройки')),
                ('end_date', models.DateField(verbose_name='Дата завершения стройки')),
                ('finish', models.BooleanField(default=False, verbose_name='Завершенный проект')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Категории продаваемых объектов')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Имя клиента')),
                ('surname', models.CharField(max_length=25, verbose_name='Фамилия клиента')),
                ('inn', models.CharField(blank=True, max_length=50, null=True, verbose_name='Инн клиента')),
                ('phone_number', models.PositiveIntegerField(verbose_name='Номер телефона клиента')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectIntoBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.PositiveIntegerField(verbose_name='Площадь объекта')),
                ('price1m', models.PositiveIntegerField(verbose_name='Цена за метр в кв.')),
                ('price_all', models.PositiveIntegerField(verbose_name='Общая цена')),
                ('rent', models.BooleanField(default=None, verbose_name='Возможность аренды')),
                ('price_category', models.CharField(blank=True, choices=[('Эконом', 'Эконом'), ('Комфорт', 'Комфорт'), ('Люкс', 'Люкс'), ('Премиум', 'Премиум')], default=None, max_length=20, null=True)),
                ('month_price', models.PositiveIntegerField(verbose_name='Цена за месяц')),
                ('book', models.BooleanField(default=False, verbose_name='Занятость объекта')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building', to='stroi.buildingobject')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object_category', to='stroi.categoryobject')),
            ],
        ),
        migrations.CreateModel(
            name='SellBuy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_of_offer', models.PositiveIntegerField(verbose_name='Сумма сделки')),
                ('offer_date', models.DateField(auto_now=True, verbose_name='Дата сделки')),
                ('sell_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_client', to='stroi.client', verbose_name='Клиент сделки')),
                ('sell_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_object', to='stroi.objectintobuilding', verbose_name='Объект сделки')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_rent_date', models.DateField(verbose_name='Дата начала аренды')),
                ('end_rent_date', models.DateField(verbose_name='Дата конца аренды')),
                ('lizing', models.BooleanField(default=False, verbose_name='Выкуп после аренды')),
                ('rent_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_client', to='stroi.client', verbose_name='Клиент взявший аренду')),
                ('rent_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_object', to='stroi.objectintobuilding', verbose_name='Арендованный объект')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=25, verbose_name='Месяц квартала')),
                ('money_for_month', models.PositiveIntegerField(verbose_name='Доход за месяц квартала')),
                ('sell_offers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_sell_offers', to='stroi.sellbuy', verbose_name='Сделки')),
                ('sell_rents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_sell_rents', to='stroi.rent', verbose_name='Аренды')),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_meeting', models.DateField(verbose_name='Дата сделки')),
                ('meeting_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calendar_client', to='stroi.client', verbose_name='Клиент встречи')),
                ('meeting_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calendar_object', to='stroi.objectintobuilding', verbose_name='Объект встречи')),
            ],
        ),
    ]
