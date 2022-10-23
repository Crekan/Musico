# Generated by Django 4.1.2 on 2022-10-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_audioarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestTracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest_title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('latest_images', models.ImageField(upload_to='latest_images/', verbose_name='Фото обложки')),
                ('latest_date_added', models.DateField(verbose_name='Дата добавления')),
                ('latest_file', models.FileField(upload_to='filr_latest_file/', verbose_name='Загрузка аудио')),
            ],
            options={
                'verbose_name': 'Последний трек',
                'verbose_name_plural': 'Последние треки',
            },
        ),
        migrations.AlterField(
            model_name='audioarea',
            name='audio_date_added',
            field=models.DateField(verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='audioarea',
            name='audio_file',
            field=models.FileField(upload_to='file_audio_area/', verbose_name='Загрузка аудио'),
        ),
        migrations.AlterField(
            model_name='audioarea',
            name='audio_images',
            field=models.ImageField(upload_to='images_audio_area/', verbose_name='Фото обложки'),
        ),
        migrations.AlterField(
            model_name='audioarea',
            name='audio_title',
            field=models.CharField(max_length=150, verbose_name='Заголовок'),
        ),
    ]
