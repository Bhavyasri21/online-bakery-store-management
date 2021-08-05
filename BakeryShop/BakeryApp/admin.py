from django.contrib import admin
from BakeryApp.models import Bakery,Bakerylist
# Register your models here.

# class AdminProduct(admin.ModelAdmin):
#     list_display = ['pname', 'price', 'category']



# class AdminCategory(admin.ModelAdmin):
#     list_display = ['name']

admin.site.register(Bakery)
admin.site.register(Bakerylist)
# admin.site.register(Product,AdminProduct)
# admin.site.register(Category,AdminCategory)

