from django.db import models


class ContactMethod(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=50)
    url = models.CharField(verbose_name="Ссылка", max_length=150, null=True, blank=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Способ связи'
        verbose_name_plural = 'Способы связи'


class LeadSource(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=50)
    url = models.CharField(verbose_name="Ссылка", max_length=150, null=True, blank=True)

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'


class TaskStatus(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=50)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Статус Задачи'
        verbose_name_plural = 'Статусы задач'


class OrderStatus(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=50)

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class ClientStatus(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=50)

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Статус клиента'
        verbose_name_plural = 'Статусы клиента'


class EmployeeGroup(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=150)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class EmployeeRole(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=50)
    group = models.ForeignKey(EmployeeGroup, verbose_name="", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
    
    
class AdminRole(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=50)

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
    
    
class ProductionType(models.Model):
    caption = models.CharField(verbose_name="Тип продукции", max_length=150)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Тип продукции'
        verbose_name_plural = 'Типы продукции'


class Tag(models.Model):
    caption = models.CharField(verbose_name="Тип продукции", max_length=150)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    
    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
