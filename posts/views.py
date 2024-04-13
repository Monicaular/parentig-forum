from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostsView(ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"
