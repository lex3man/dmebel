from django.contrib import admin
from .models import LeadSource, ContactMethod, EmployeeRole, ClientStatus, OrderStatus, ProductionType, TaskStatus, AdminRole, Tag, EmployeeGroup


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


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('caption',)


@admin.register(ProductionType)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('caption', 'description')


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('caption',)


@admin.register(AdminRole)
class AdminRoleAdmin(admin.ModelAdmin):
    list_display = ('caption',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)


@admin.register(EmployeeGroup)
class EmployeeGroupAdmin(admin.ModelAdmin):
    list_display = ('caption', 'description')
