from django.contrib import admin

from .models import User
from .models import Store
from .models import Order
from .models import Address

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User
    can_delete = True
    verbose_name_plural = 'users'
    list_display = ('user_id', 'email', 'password', 'fname', 'lname')

class AddressAdmin(admin.ModelAdmin):
    model = Address
    can_delete = True
    verbose_name_plural = 'addresses'
    list_display = ('user', 'street_address', 'line_number', 'city', 'state', 'zip_code')

class StoreAdmin(admin.ModelAdmin):
    model = Store
    can_delete = True
    verbose_name_plural = 'stores'
    list_display = ('latitude', 'longitude')

class OrderAdmin(admin.ModelAdmin):
    model = Order
    can_delete = True
    verbose_name_plural = 'orders'
    list_display = ('total','timestamp')


admin.site.register(Address, AddressAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(User, UserAdmin)
