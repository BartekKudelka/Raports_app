
# Register your models here.

from django.contrib import admin

from .models import User, Product, Client, Invoice, Report, Purchase

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(Report)
admin.site.register(Purchase)