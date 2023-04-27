from django.urls import path
from .views import Bot, BotConf

urlpatterns = [
    path('bot/', Bot.as_view(), name='bot'),
    path('bot/<str:caption>', BotConf.as_view(), name='bot_conf')
]

