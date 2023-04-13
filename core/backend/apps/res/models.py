from django.db import models
from ..data.models import ClientStatus, EmployeeRole, AdminRole


class Human(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=500)
    name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50, null=True, blank=True)
    father_name = models.CharField(verbose_name="Отчество", max_length=50, null=True, blank=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=20, null=True, blank=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"


class Admin(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=500)
    human = models.ForeignKey(Human, verbose_name="Субъект", on_delete=models.CASCADE)
    role = models.ForeignKey(AdminRole, verbose_name="Роль", on_delete=models.SET_NULL, null=True)
                              
    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"


class Employee(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=500)
    human = models.ForeignKey(Human, verbose_name="Субъект", on_delete=models.CASCADE)
    role = models.ForeignKey(EmployeeRole, verbose_name="Должность", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Client(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=500)
    human = models.ForeignKey(Human, verbose_name="Субъект", on_delete=models.CASCADE)
    status = models.ForeignKey(ClientStatus, verbose_name="Статус", on_delete=models.SET_NULL, null=True)
    address = models.CharField(verbose_name="Адрес", max_length=200, null=True, blank=True)
    comments = models.TextField(verbose_name="Комментарии", null=True, blank=True)
    
    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

