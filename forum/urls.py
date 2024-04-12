from django.contrib import admin
from django.urls import path
from posts.views import my_post

urlpatterns = [
    path('posts/', my_post, name='posts'),
    path('admin/', admin.site.urls),
]
