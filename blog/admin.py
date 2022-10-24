from django.contrib import admin
from .models import *


class BlogsCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("categories_name",)}


admin.site.register(BlogPosts)
admin.site.register(BlogsCategories, BlogsCategoriesAdmin)
admin.site.register(RecentPost)
admin.site.register(InstagramFeeds)
admin.site.register(AuthorBlog)
admin.site.register(Like)
