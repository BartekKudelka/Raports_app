
# Register your models here.

from django.contrib import admin

from .models import Product, Client, Invoice, Report, InvoiceItem

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(Report)
admin.site.register(InvoiceItem)