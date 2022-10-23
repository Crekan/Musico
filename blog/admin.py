from django.contrib import admin
from .models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')


admin.site.register(Comment, CommentAdmin)
admin.site.register(BlogPosts)
admin.site.register(BlogsCategories)
admin.site.register(RecentPost)
admin.site.register(InstagramFeeds)
admin.site.register(AuthorBlog)
