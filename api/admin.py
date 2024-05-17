from django.contrib import admin

from api.models import Category, Product,  About, Contact, Worker 

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(About)
admin.site.register(Worker)
admin.site.register(Contact)