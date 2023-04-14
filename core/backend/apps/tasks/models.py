from django.db import models
from ..crm.models import Order
from ..res.models import Client, Employee
from ..data.models import TaskStatus


class Project(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=100)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class CheckPoint(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=100)
    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Контрольная точка'
        verbose_name_plural = 'Контрольные точки'


class Task(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=100)
    project = models.ForeignKey(Project, verbose_name="Проект", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name="Заказ", on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(TaskStatus, verbose_name="Статус", on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, verbose_name="Клиент", on_delete=models.SET_NULL, null=True)
    init_empl = models.ForeignKey(Employee, related_name="init_empl", verbose_name="Постановщик задачи", on_delete=models.SET_NULL, null=True)
    maker = models.ForeignKey(Employee, related_name="maker", verbose_name="Ответственный", on_delete=models.SET_NULL, null=True)
    deadline = models.DateTimeField(verbose_name="Завершение")

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Report(models.Model):
    caption = models.CharField(verbose_name="Наименвание", max_length=100)
    date = models.DateTimeField(verbose_name="Сформирован")
    content = models.TextField(verbose_name="Содержание отчёта")

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
