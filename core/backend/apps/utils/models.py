import subprocess, os, redis, signal
from django.db import models
from django.contrib import admin

bots_status_base = redis.ConnectionPool(host='redis', port=6379, db=0)
bots_status = redis.Redis(connection_pool=bots_status_base, charset="utf-8", decode_responses=True)
bot_init_script = 'bot/starter.py'


class Bot(models.Model):
    caption = models.CharField(verbose_name = 'Наименование бота', max_length=50)
    tgbot_token = models.CharField(verbose_name = 'Telegram API токен', max_length=50)
    start_message = models.TextField(verbose_name = 'Текст приветственного сообщения на команду "/start"')
    active = models.BooleanField(verbose_name='Работает', default=False)
    
    def __str__(self):
        return self.caption

    @admin.action(description = 'Запустить выбранных ботов')
    def start(self, _, queryset):
        for bot in queryset:
            if not bot.active:
                process = subprocess.Popen(['python', bot_init_script, bot.tgbot_token])
                bots_status.set(bot.caption, process.pid)
                bot.active = True
                bot.save()

    @admin.action(description = 'Остановить выбранных ботов')
    def stop(self, _, queryset):
        for bot in queryset:
            if bot.active:
                pid = bots_status.get(bot.caption)
                if pid != None:
                    os.kill(int(pid), signal.SIGKILL)
                    bots_status.delete(bot.caption)
                bot.active = False
                bot.save()

    class Meta:
        verbose_name = 'Телеграм бот'
        verbose_name_plural = 'Телеграм боты'
