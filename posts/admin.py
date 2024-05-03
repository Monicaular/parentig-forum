from django.contrib import admin
from .models import Post, Tag, Comment, Resource, ResourceLink, ContactRequest, Rule


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin interface options for Posts.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        list_filter (tuple): Fields to filter in the admin list view.
        search_fields (tuple): Fields to search in the admin list view.
        list_editable (tuple): Fields that can be edited directly in the admin list view.
    """
    list_display = ('title', 'author', 'created_at', 'updated_at', 'is_featured', )
    list_filter = ('author', 'updated_at', 'is_featured', )
    search_fields = ('title', 'content')
    list_editable = ('is_featured', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Admin interface options for Tags.
    
    Attributes:
        list_display (tuple): Fields to display in the admin list view.
    """
    list_display = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface options for Comments.
    
    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        list_filter (tuple): Fields to filter in the admin list view.
        search_fields (tuple): Fields to search in the admin list view.
    """
    list_display = ('post', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('content',)

admin.site.register(Resource)
"""
Admin interface options for Resources.
"""

admin.site.register(ResourceLink)
"""
Admin interface options for Resource Links.
"""

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    """
    Admin interface options for Contact Requests.
    
    Attributes:
        list_display (tuple): Fields to display in the admin list view.
    """
    list_display = ('message', 'read',)

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    """
    Admin interface options for Rules.
    
    Attributes:
        list_display (list): Fields to display in the admin list view.
    """
    list_display = ['title', 'description']