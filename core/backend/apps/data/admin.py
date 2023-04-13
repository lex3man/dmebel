from django.contrib import admin
from .models import LeadSource, ContactMethod, EmployeeRole, ClientStatus


@admin.register(LeadSource)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('caption', 'url')


@admin.register(ContactMethod)
class MethodsAdmin(admin.ModelAdmin):
    list_display = ('caption', 'url')


@admin.register(EmployeeRole)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('caption',)


@admin.register(ClientStatus)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('caption',)
