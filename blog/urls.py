from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', Blog.as_view(), name='blog'),
    path('blog/<slug:categories_blog>/', ShowPost.as_view(), name='detail'),
    # path('blog/<int:categories_blog>/', com, name='detail'),
    path('categories/<slug:categories_slug>/', ShowCategories.as_view(), name='show_categories'),
    path('search/', Search.as_view(), name='search'),
    path('like/', like_post, name='like-post'),
]
