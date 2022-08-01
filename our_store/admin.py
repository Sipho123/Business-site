from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)