from django.db import models


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=255, verbose_name='Токен')
    tg_chat = models.CharField(max_length=255, verbose_name='Чат')
    tg_message = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'