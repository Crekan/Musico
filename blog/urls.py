from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', Blog.as_view(), name='blog'),
    path('blog/<int:categories_blog>/', ShowPost.as_view(), name='detail'),
    path('categories/<int:categories_int>/', ShowCategories.as_view(), name='show_categories'),
    path('search/', Search.as_view(), name='search'),
]
