from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from .models import *


def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = BlogPosts.objects.get(id=post_id)

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()

    return redirect(post_obj)


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


class Search(ListView):
    context_object_name = 'posts'
    template_name = 'blog/blog.html'

    def get_queryset(self):
        return BlogPosts.objects.filter(blog_title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        context['categories_blog'] = BlogsCategories.objects.all()
        return context


class ShowPost(DetailView):
    model = BlogPosts
    template_name = 'blog/single-blog.html'
    slug_url_kwarg = 'categories_blog'
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_blog'] = BlogsCategories.objects.all()
        context['author'] = AuthorBlog.objects.all()
        return context


class ShowCategories(ListView):
    model = BlogPosts
    template_name = 'blog/blog.html'
    context_object_name = 'categories_blog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = BlogPosts.objects.filter(blog_category__slug=self.kwargs['categories_slug'])
        context['categories_blog'] = BlogsCategories.objects.all()
        context['recent_post_blog'] = RecentPost.objects.all()
        context['images_instagram'] = InstagramFeeds.objects.all()
        return context
