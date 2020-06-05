from django.contrib import admin

# Register your models here.
from .models import Product,Designer

from .models import Registerpage


admin.site.register(Product)
admin.site.register(Registerpage)
admin.site.register(Designer)
