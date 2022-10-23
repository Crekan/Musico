from django.db import models


class ImageModel(models.Model):
    place = models.CharField(max_length=255, verbose_name='Место')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class GalleriesModel(models.Model):
    galleries_img = models.ImageField(upload_to='galleries/', verbose_name='Галерея')

    def __str__(self):
        return f'Изображение - {self.pk}'

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'


class AudioArea(models.Model):
    audio_title = models.CharField(max_length=150, verbose_name='Заголовок')
    audio_images = models.ImageField(upload_to='images_audio_area/', verbose_name='Фото обложки')
    audio_date_added = models.DateField(verbose_name='Дата добавления')
    audio_file = models.FileField(upload_to='file_audio_area/', verbose_name='Загрузка аудио')

    def __str__(self):
        return self.audio_title

    class Meta:
        verbose_name = 'Аудио зона'
        verbose_name_plural = 'Аудио зоны'


class LatestTracks(models.Model):
    latest_title = models.CharField(max_length=150, verbose_name='Заголовок')
    latest_images = models.ImageField(upload_to='latest_images/', verbose_name='Фото обложки')
    latest_date_added = models.DateField(verbose_name='Дата добавления')
    latest_file = models.FileField(upload_to='filr_latest_file/', verbose_name='Загрузка аудио')

    def __str__(self):
        return self.latest_title

    class Meta:
        verbose_name = 'Последний трек'
        verbose_name_plural = 'Последние треки'


class AboutArea(models.Model):
    area_images = models.ImageField(upload_to='area_images/', verbose_name='Изображение')
    area_title = models.CharField(max_length=150, verbose_name='Заголовок')
    area_descriptions = models.TextField(verbose_name='Описание')
    area_painting = models.ImageField(upload_to='area_images/', verbose_name='Роспись', null=True)

    def __str__(self):
        return self.area_title

    class Meta:
        verbose_name = 'О районе'
        verbose_name_plural = 'О районах'