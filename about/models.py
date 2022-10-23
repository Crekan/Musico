from django.db import models


class AboutVideo(models.Model):
    about_video = models.CharField(max_length=250, verbose_name='URL на видео в Ютубе')
    about_images = models.ImageField(upload_to='about_images/', verbose_name='Превью', null=True)

    def __str__(self):
        return f'Виедо - {self.pk}'

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'