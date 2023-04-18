
from django.db import models

class Module(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='Порядковый номер', unique=True)
    title = models.CharField(verbose_name='Название', max_length=105)
    description = models.TextField(verbose_name='Описание')


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ["number"]

    def __str__(self):
        return self.title