from django.db import models
from django.contrib import admin


class Bot(models.Model):
    caption = models.CharField(verbose_name = 'Наименование бота', max_length=50)
    tgbot_token = models.CharField(verbose_name = 'Telegram API токен', max_length=50)
    start_message = models.TextField(verbose_name = 'Текст приветственного сообщения на команду "/start"')
    active = models.BooleanField(verbose_name='Работает', default=False)
    
    def __str__(self):
        return self.caption

    @admin.action(description = 'Запустить выбранных ботов')
    def start(self, request, queryset):
        for b in queryset:
            if not b.active:
                b.active = True
                b.save()

    @admin.action(description = 'Остановить выбранных ботов')
    def stop(self, request, queryset):
        for b in queryset:
            if b.active:
                b.active = False
                b.save()
