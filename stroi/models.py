from django.db import models
import datetime


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=25, null=False,
                            blank=False, verbose_name='Имя клиента')
    surname = models.CharField(max_length=25, null=False,
                               blank=False, verbose_name='Фамилия клиента')
    inn = models.CharField(max_length=50, null=True,
                           blank=True, verbose_name='Инн клиента')
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефона клиента')

    def __str__(self):
        return str(self.surname)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class BuildingObject(models.Model):
    CHUI = 'Чуйская'
    TALAS = 'Таласская'
    BATKEN = 'Баткенская'
    ISSYK_KYL = 'Иссык-кульская'
    NARYN = 'Нарынская'
    OSH = 'Ошская'
    JALAL_ABAD = 'Джалал-Абадская'

    REGION_CHOICES = [
        (CHUI, 'Чуйская'),
        (TALAS, 'Таласская'),
        (BATKEN, 'Баткенская'),
        (ISSYK_KYL, 'Иссык-кульская'),
        (NARYN, 'Нарынская'),
        (OSH, 'Ошская'),
        (JALAL_ABAD, 'Джалал-Абадская'),
    ]
    region = models.CharField(choices=REGION_CHOICES, max_length=20,
                              verbose_name='Регион')
    address = models.CharField(max_length=30, null=False,
                               blank=True, verbose_name='Адрес объекта')
    start_date = models.DateField(verbose_name='Дата начала стройки')
    end_date = models.DateField(verbose_name='Дата завершения стройки')
    finish = models.BooleanField(verbose_name='Завершенный проект',
                                 default=False)

    def __str__(self):
        return str(self.address)

    class Meta:
        verbose_name = 'Объект Здание'
        verbose_name_plural = 'Объекты Здания'


class CategoryObject(models.Model):
    name = models.CharField(max_length=45, verbose_name='Категории продаваемых объектов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория Объекта'
        verbose_name_plural = 'Категории Объектов'


class ObjectIntoBuilding(models.Model):
    ECONOMY = 'Эконом'
    COMFORT = 'Комфорт'
    LUX = 'Люкс'
    PREMIUM = 'Премиум'

    PRICE_CATEGORY_CHOICES = [
        (ECONOMY, 'Эконом'),
        (COMFORT, 'Комфорт'),
        (LUX, 'Люкс'),
        (PREMIUM, 'Премиум'),
    ]
    area = models.PositiveIntegerField(verbose_name='Площадь объекта')
    price1m = models.PositiveIntegerField(verbose_name='Цена за метр в кв.')
    price_all = models.PositiveIntegerField(verbose_name='Общая цена')
    rent = models.BooleanField(default=None, verbose_name='Возможность аренды')
    price_category = models.CharField(choices=PRICE_CATEGORY_CHOICES, max_length=20,
                                      default=None, null=True,
                                      blank=True, verbose_name='Ценовая категория')
    month_price = models.PositiveIntegerField(verbose_name='Цена за месяц')
    book = models.BooleanField(verbose_name='Занятость объекта', default=False)
    building = models.ForeignKey(BuildingObject, on_delete=models.CASCADE,
                                 related_name='building')
    category = models.ForeignKey(CategoryObject, on_delete=models.CASCADE,
                                 related_name='object_category', verbose_name='Категория объекта')

    def __str__(self):
        return str(self.building.address)

    class Meta:
        verbose_name = 'Объект Помещение'
        verbose_name_plural = 'Объекты Помещения'

    @property
    def sell_or_rent(self):
        try:
            a = Rent.objects.filter(rent_object=self)
            b = SellBuy.objects.filter(sell_object=self)
            if a == None:
                return 'Нет'
            elif b == None:
                return 'Нет'
            else:
                return "Да"
        except Exception as e:
            print(str(e))


class Rent(models.Model):
    start_rent_date = models.DateField(verbose_name='Дата начала аренды')
    end_rent_date = models.DateField(verbose_name='Дата конца аренды')
    rent_client = models.ForeignKey(Client, verbose_name='Клиент взявший аренду',
                                    on_delete=models.CASCADE, related_name='rent_client')
    rent_object = models.ForeignKey(ObjectIntoBuilding, verbose_name='Арендованный объект',
                                    on_delete=models.CASCADE, related_name='rent_object')
    lizing = models.BooleanField(verbose_name='Выкуп после аренды', default=False)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Сделка Аренды'
        verbose_name_plural = 'Сделки Аренды'

    # @property
    # def now_total_price(self):
    #     now = datetime.datetime.now().date()
    #     start_date = self.start_rent_date
    #     rent_days = now - start_date
    #
    #     pass


class SellBuy(models.Model):
    sell_object = models.ForeignKey(ObjectIntoBuilding, verbose_name='Объект сделки',
                                    on_delete=models.CASCADE, related_name='sell_object_build')
    sell_client = models.ForeignKey(Client, verbose_name='Клиент сделки',
                                    on_delete=models.CASCADE, related_name='sell_client')
    sum_of_offer = models.PositiveIntegerField(verbose_name='Сумма сделки')
    offer_date = models.DateField(verbose_name='Дата сделки', auto_now=True)

    def __str__(self):
        return 'Сделка' + " " + str(self.sell_client.name) + " " + str(self.offer_date)

    class Meta:
        verbose_name = 'Сделка Купли-Продажи'
        verbose_name_plural = 'Сделки Купли-Продажи'


class Income(models.Model):
    sell_offers = models.ForeignKey(SellBuy, verbose_name='Сделки',
                                    on_delete=models.CASCADE, related_name='income_sell_offers')
    sell_rents = models.ForeignKey(Rent, verbose_name='Аренды',
                                   on_delete=models.CASCADE, related_name='income_sell_rents')
    month = models.CharField(max_length=25, verbose_name='Месяц квартала')
    money_for_month = models.PositiveIntegerField(verbose_name='Доход за месяц квартала')

    def __str__(self):
        return str(self.month) + ' ' + str(self.money_for_month)

    class Meta:
        verbose_name = 'Доход за месяц'
        verbose_name_plural = 'Доход за месяц'


class Calendar(models.Model):
    date_meeting = models.DateField(verbose_name='Дата сделки')
    meeting_client = models.ForeignKey(Client, verbose_name='Клиент встречи',
                                       on_delete=models.CASCADE, related_name='calendar_client')
    meeting_object = models.ForeignKey(ObjectIntoBuilding, verbose_name='Объект встречи',
                                       on_delete=models.CASCADE, related_name='calendar_object')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Расписание встреч с клиентами'
        verbose_name_plural = 'Расписание встреч с клиентами'

