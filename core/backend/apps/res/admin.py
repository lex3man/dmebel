from django.contrib import admin
from .models import Human, Client, Employee, Admin


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ('caption', 'phone_number', 'comments')
    readonly_fields = ('caption',)
    # list_filter = ()
    search_fields = ('caption', 'phone_number', 'comments')
    # actions = []


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ()
    # readonly_fields = ()
    # list_filter = ()
    # search_fields = ()
    # actions = []


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ()
    # readonly_fields = ()
    # list_filter = ()
    # search_fields = ()
    # actions = []


@admin.register(Admin)
class AdmiAdmin(admin.ModelAdmin):
    list_display = ()
    # readonly_fields = ()
    # list_filter = ()
    # search_fields = ()
    # actions = []
