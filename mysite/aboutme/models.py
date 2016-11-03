from django.db import models


# Create your models here.
class Work(models.Model):
    organization = models.CharField(verbose_name='Организация', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=32, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=32)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Время работы', default=1)
