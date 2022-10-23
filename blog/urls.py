from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', Blog.as_view(), name='blog'),
    path('blog/<int:categories_blog>/', detail, name='detail'),
    path('categories_id/<int:categories_id>/', show_categories, name='show_categories'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
