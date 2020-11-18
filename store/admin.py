from django.contrib import admin
from .models import *

admin.site.site_header = 'Austin Ford Admin'
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
