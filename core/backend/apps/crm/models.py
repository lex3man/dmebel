from django.db import models
from ..res.models import Client
from ..data.models import OrderStatus, ProductionType


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
    preorder = models.ForeignKey(PreOrder, related_name="from_preorder", verbose_name="Предзаказ", on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(OrderStatus, verbose_name="Статус заказа", on_delete=models.SET_NULL, null=True)
    prod_type = models.ForeignKey(ProductionType, verbose_name="Тип продукции", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
