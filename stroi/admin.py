from django.contrib import admin
from .models import *
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'surname', 'inn',
                    'phone_number')
    search_fields = ['name', 'surname']


class RentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'start_rent_date', 'end_rent_date', 'client_surname', 'lizing')
    list_filter = ('rent_object__book', 'lizing')

    def client_surname(self, obj):
        return obj.rent_client.surname

    client_surname.short_description = "Фамилия клиента"


class ObjectIntoBuildAdmin(admin.ModelAdmin):
    list_display = ('pk', 'area', 'price1m',
                    'price_all',
                    'category', 'price_category', 'sell_or_rent_admin',
                    'month_price')
    list_filter = ('category__name', 'price_category', 'rent')
    ordering = ('price_all', 'month_price')

    def sell_or_rent_admin(self, obj):
        return obj.sell_or_rent

    sell_or_rent_admin.short_description = "Сделка на объект"


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_meeting', 'meeting_client', 'meeting_object')
    # search_fields = ['name', 'surname']


class BuildingObjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'address', 'region', 'start_date', 'end_date',
                    'finish')
    list_filter = ('region', 'finish')


admin.site.register(Client, ClientAdmin)
admin.site.register(BuildingObject, BuildingObjectAdmin)
admin.site.register(CategoryObject)
admin.site.register(ObjectIntoBuilding, ObjectIntoBuildAdmin)
admin.site.register(Rent, RentAdmin)
admin.site.register(SellBuy)
admin.site.register(Income)
admin.site.register(Calendar, CalendarAdmin)
