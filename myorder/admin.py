from django.contrib import admin
from .models import Order,Category
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','product_name','product_category','AddHolder_name','place','start_date','end_date', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ['user','product_name']
    readonly_fields = ('user',)


admin.site.register(Order ,OrderAdmin)
admin.site.register(Category)