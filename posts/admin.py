from django.contrib import admin
from .models import Post, Tag, Comment, Resource


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'updated_at')
    search_fields = ('title', 'content')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('content',)

admin.site.register(Resource)