from django.db import models


class Human(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=500)
    name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50, null=True, blank=True)
    father_name = models.CharField(verbose_name="Отчество", max_length=50, null=True, blank=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=20, null=True, blank=True)
    comments = models.TextField(verbose_name="Комментарии", null=True, blank=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"


class Admin(Human):
    pass


class Employee(Human):
    pass


class Client(Human):
    pass
