from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post

class PostsView(ListView):
    queryset = Post.objects.all().order_by("-created_at")
    template_name = "posts/post_list.html"
    paginate_by = 4

class HomeView(TemplateView):
    template_name = 'posts/index.html'
