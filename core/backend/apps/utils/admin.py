from django.contrib import admin
from .models import Bot


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('caption', 'active')
    actions = [Bot.start, Bot.stop]
    readonly_fields = ('active',)
