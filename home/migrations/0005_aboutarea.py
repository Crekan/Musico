# Generated by Django 4.1.2 on 2022-10-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_latesttracks_alter_audioarea_audio_date_added_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_images', models.ImageField(upload_to='area_images/', verbose_name='Изображение')),
                ('area_title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('area_descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'О районе',
                'verbose_name_plural': 'О районах',
            },
        ),
    ]
