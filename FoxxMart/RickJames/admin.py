from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(RickJamesCustomer)
admin.site.register(RickJamesProduct)
admin.site.register(RickJamesOrder)
admin.site.register(RickJamesOrderItem)
admin.site.register(RickJamesShippingAddress)
