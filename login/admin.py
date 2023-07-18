from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserReg
from django.contrib.auth.models import Group


admin.site.site_header = "Marketing's Admin Panel"
admin.site.site_title = "Marketing's Admin Panel"
admin.site.unregister(Group)


class SuperuserProxy(UserReg):
    class Meta:
        proxy = True
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def get_queryset(self):
        return super().get_queryset().filter(is_superuser=True)

class RegularUserProxy(UserReg):
    class Meta:
        proxy = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_queryset(self):
        return super().get_queryset().filter(is_superuser=False)

@admin.register(SuperuserProxy)
class SuperuserAdmin(UserAdmin):
    model = SuperuserProxy

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=True)
    
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    readonly_fields = ('username', 'last_login', 'date_joined', 'first_name', 'last_name', 'email')
    list_display = ('username' , 'email' , 'is_active')
    search_fields = ['username','email']
    list_filter = ('is_active',)

@admin.register(RegularUserProxy)
class RegularUserAdmin(UserAdmin):
    model = RegularUserProxy

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=False)
    
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'image')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('username', 'last_login', 'date_joined', 'first_name', 'last_name', 'email', 'image')
    list_display = ('username' , 'email' , 'is_active')
    search_fields = ['username','email']
    list_filter = ('is_active',)




