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


class Contract(models.Model):
    current_id = models.CharField(verbose_name='current_id', max_length=4)
    contract_number = models.CharField(verbose_name='Дата договора', max_length=32)
    contract_date = models.DateField(auto_now=True)
    ooo_name = models.CharField(verbose_name='Контрагент', max_length=64)
    contract_status = models.CharField(verbose_name='Статус договора', max_length=32)
    ooo_address = models.CharField(verbose_name='Физический адрес', max_length=64)
    ooo_e_mail = models.EmailField(verbose_name='@')
    month1 = models.PositiveIntegerField(verbose_name='Месяц 1')
    month2 = models.PositiveIntegerField(verbose_name='Месяц 2')