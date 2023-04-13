from django.db import models
from ..res.models import Client


class PreOrder(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=150)
    client = models.ForeignKey(Client, verbose_name="Клиент", on_delete=models.CASCADE)
    details = models.TextField(verbose_name="Детали")

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Предзаказ'
        verbose_name_plural = 'Предзаказы'


class Order(PreOrder):
    pass
