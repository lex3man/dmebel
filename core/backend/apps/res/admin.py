from django.contrib import admin
from .models import Human, Client, Employee, Admin


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ('caption', 'phone_number')
    # readonly_fields = ('caption',)
    # list_filter = ()
    search_fields = ('caption', 'phone_number')
    # actions = []


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('caption', 'status', 'comments')
    # readonly_fields = ()
    list_filter = ('status', 'tag')
    search_fields = ('caption', 'human', 'comments')
    # actions = []
    fieldsets = (
            ( 'Клиент', {'fields': ('caption', 'human', 'status')} ),
            ( 'Дополнительно', {'fields': ('address', 'comments', 'method')} ),
            ( 'Тэги', {'fields': ('tag',)} ),
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('caption', 'role')
    # readonly_fields = ()
    list_filter = ('role', 'tag')
    # search_fields = ()
    # actions = []


@admin.register(Admin)
class AdmiAdmin(admin.ModelAdmin):
    list_display = ('caption', 'role')
    # readonly_fields = ()
    list_filter = ('role',)
    # search_fields = ()
    # actions = []
