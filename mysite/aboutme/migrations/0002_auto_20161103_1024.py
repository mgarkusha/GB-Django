# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=32, verbose_name='ФИО')),
                ('birthday', models.CharField(max_length=32, verbose_name='Дата рождения')),
                ('profession', models.CharField(max_length=32, verbose_name='Специальность')),
                ('born_place', models.CharField(max_length=32, verbose_name='Место рождения')),
                ('hobby', models.CharField(max_length=32, verbose_name='Хобби')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=32, verbose_name='Наименование учреждения')),
                ('learn_time', models.PositiveIntegerField(verbose_name='Период учёбы')),
                ('profession', models.CharField(max_length=32, verbose_name='Учёная степень')),
            ],
        ),
        migrations.RemoveField(
            model_name='work',
            name='duties',
        ),
        migrations.RemoveField(
            model_name='work',
            name='period',
        ),
        migrations.RemoveField(
            model_name='work',
            name='site',
        ),
    ]
