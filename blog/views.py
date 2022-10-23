from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import *


class Blog(ListView):
    model = BlogPosts
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return BlogPosts.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_blog'] = BlogsCategories.objects.all()
        context['recent_post_blog'] = RecentPost.objects.all()
        context['images_instagram'] = InstagramFeeds.objects.all()
        return context


class SearchResultsView(ListView):
    model = BlogPosts
    template_name = 'blog/blog.html'

    def get_queryset(self):
        return BlogPosts.objects.filter(name__icontains='test s')


def detail(request, categories_blog):
    post = get_object_or_404(BlogPosts, pk=categories_blog)
    posts = BlogPosts.objects.filter(pk=categories_blog)
    сategory_blog = BlogsCategories.objects.all()
    posts_details = DetailsBlog.objects.filter(pk=categories_blog)
    recent_post_blog = RecentPost.objects.all()
    images_instagram = InstagramFeeds.objects.all()

    context = {
        'post': post,
        'posts': posts,
        'сategory_blog': сategory_blog,
        'posts_details': posts_details,
        'recent_post_blog': recent_post_blog,
        'images_instagram': images_instagram,
    }
    return render(request, 'blog/single-blog.html', context)


def show_categories(request, categories_id):
    posts = BlogPosts.objects.filter(blog_category=categories_id)
    categories_blog = BlogsCategories.objects.all()

    context = {
        'posts': posts,
        'categories_blog': categories_blog,
    }

    return render(request, 'blog/blog.html', context)
