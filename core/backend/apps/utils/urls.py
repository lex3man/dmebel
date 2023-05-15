from django.urls import path
from .views import Bots, BotConf

urlpatterns = [
    path('bot/', Bots.as_view(), name='bot'),
    path('bot/<str:pk>', BotConf.as_view(), name='bot_conf')
]

