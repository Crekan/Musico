from django.contrib import admin
from .models import *


class BlogsCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("categories_name",)}


class BlogPostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("blog_title",)}


admin.site.register(BlogPosts, BlogPostsAdmin)
admin.site.register(BlogsCategories, BlogsCategoriesAdmin)
admin.site.register(RecentPost)
admin.site.register(InstagramFeeds)
admin.site.register(AuthorBlog)
admin.site.register(Like)
admin.site.register(CommentPost)
