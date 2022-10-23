from django.db import models


class TracksMusicArea(models.Model):
    tracks_images = models.ImageField(upload_to='tracks_images/', verbose_name='Обложка')
    tracks_title = models.CharField(max_length=150, verbose_name='Название трека')
    tracks_date_added = models.DateField(verbose_name='Дата добавления')
    tracks_music = models.FileField(upload_to='tracks_music/', verbose_name='Загрузка трека')

    def __str__(self):
        return self.tracks_title

    class Meta:
        verbose_name = 'Мои треки'
        verbose_name_plural = 'Мои треки'
