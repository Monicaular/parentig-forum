from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostsView(ListView):
    queryset = Post.objects.all().order_by("-created_at")
    template_name = "post_list.html"
