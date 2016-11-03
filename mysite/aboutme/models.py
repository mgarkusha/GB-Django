from django.db import models


# Create your models here.
class Work(models.Model):
    organization = models.CharField(verbose_name='Организация', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=32)

class Education(models.Model):
    organization = models.CharField(verbose_name='Наименование учреждения', max_length=32)
    learn_time = models.PositiveIntegerField(verbose_name='Период учёбы')
    profession = models.CharField(verbose_name='Учёная степень', max_length=32)

class About(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=32)
    birthday = models.CharField(verbose_name='Дата рождения', max_length=32)
    profession = models.CharField(verbose_name='Специальность', max_length=32)
    born_place = models.CharField(verbose_name='Место рождения', max_length=32)
    hobby = models.CharField(verbose_name='Хобби', max_length=32)
