from django.urls import path
from .views import GetRes

urlpatterns = [
    path('tokens/', GetRes.as_view()),
]
