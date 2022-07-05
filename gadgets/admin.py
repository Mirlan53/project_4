from django.contrib import admin
from gadgets.models import Manufacturer, ProductCategory, Product

admin.site.register(Manufacturer)
admin.site.register(ProductCategory)
admin.site.register(Product)