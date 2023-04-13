from django.contrib import admin
from .models import PreOrder, Order


@admin.register(PreOrder)
class PreorderAdmin(admin.ModelAdmin):
    list_display = ('caption', 'client', 'details')
    list_filter = ('client',)
    search_fields = ('details', 'caption')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('caption', 'client', 'details')
    list_filter = ('client', 'prod_type')
    search_fields = ('details', 'caption', 'preorder')
