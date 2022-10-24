from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('BlogPosts', on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)


class BlogPosts(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)
    blog_images = models.ImageField(upload_to='blog_images/', verbose_name='Фото')
    blog_title = models.CharField(max_length=150, verbose_name='Заголовок', unique=True)
    blog_descriptions = models.TextField(verbose_name='Описание')
    blog_who_posted = models.CharField(max_length=150, verbose_name='Кто опубликовал пост')
    blog_comments = models.CharField(max_length=150, verbose_name='Коментарии')
    blog_date_added = models.DateField(verbose_name='Дата добавления')
    blog_cards = models.TextField(verbose_name='Карточка', null=True)
    blog_category = models.ForeignKey('BlogsCategories', on_delete=models.PROTECT, verbose_name='Категория поста',
                                      null=True)
    likes = models.ManyToManyField(User, blank=True, default=None, related_name='liked')

    @property
    def num_likes(self):
        return self.likes.all().count()

    def __str__(self):
        return self.blog_title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

    def get_absolute_url(self):
        return reverse('detail', kwargs={
            'categories_blog': self.slug
        })


class BlogsCategories(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)
    categories_name = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self):
        return self.categories_name

    class Meta:
        verbose_name = 'Категория Блога'
        verbose_name_plural = 'Категории Блога'

    def get_absolute_url(self):
        return reverse('show_categories', kwargs={
            'categories_slug': self.slug
        })


class RecentPost(models.Model):
    recent_title = models.CharField(max_length=250, verbose_name='Заголовок')
    recent_date_added = models.DateField(verbose_name='Дата добавления')
    recent_images = models.ImageField(upload_to='recent_post/', verbose_name='Фото')

    def __str__(self):
        return self.recent_title

    class Meta:
        verbose_name = 'Недавний посты'
        verbose_name_plural = 'Недавние посты'


class InstagramFeeds(models.Model):
    instagram_images = models.ImageField(upload_to='instagram_feeds/', verbose_name='Фото из Инсты')

    def __str__(self):
        return f'Id Images - {self.pk}'

    class Meta:
        verbose_name = 'Instagram'
        verbose_name_plural = 'Instagram'


class AuthorBlog(models.Model):
    author_images = models.ImageField(upload_to='author_images/', verbose_name='Фото')
    author_title = models.CharField(max_length=150, verbose_name='Имя')
    author_descriptions = models.CharField(max_length=255, verbose_name='Описание')

    def __str__(self):
        return self.author_title

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автор'
