from django.contrib import admin
from .models import Product,Brand,Address,Category,Feedback

class productAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('title', 'price','is_bestseller')
    list_filter = ('is_bestseller',)
    search_fields = ('title', 'category')

# Register your models here
admin.site.register(Brand)
admin.site.register(Feedback)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Product,productAdmin)
