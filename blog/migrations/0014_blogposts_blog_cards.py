# Generated by Django 4.1.2 on 2022-10-23 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_delete_detailsblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogposts',
            name='blog_cards',
            field=models.TextField(null=True, verbose_name='Карточка'),
        ),
    ]