from django.contrib import admin
from .models import Store
from .models import Product
from .models import Client
from .models import Order

# Register your models here.
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)
