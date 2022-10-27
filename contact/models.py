from django.db import models


class Locate(models.Model):
    place_title = models.CharField(max_length=250, verbose_name='Место')
    place_description = models.CharField(max_length=250, verbose_name='Описание места')

    number = models.CharField(max_length=250, verbose_name='Телефон')
    working_hours = models.CharField(max_length=250, verbose_name='Часы работы')

    email = models.EmailField(verbose_name='Email')
    email_description = models.CharField(max_length=250, verbose_name='Описание Email')

    def __str__(self):
        return self.place_title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Место'


class GetInTouch(models.Model):
    text = models.TextField(verbose_name='')
    name = models.CharField(max_length=250, verbose_name='')
    get_in_touch_email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=255, verbose_name='')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Связаться'
        verbose_name_plural = 'Связаться'
