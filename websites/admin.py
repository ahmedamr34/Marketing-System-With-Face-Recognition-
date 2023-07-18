from django.contrib import admin
from .models import Place,AddHolder



class AddHolderAdmin(admin.ModelAdmin):
    list_display = ('name' , 'place' , 'price' ,)
    ordering = ('name',)
    search_fields = ('name',)


admin.site.register(AddHolder ,AddHolderAdmin)
admin.site.register(Place)

