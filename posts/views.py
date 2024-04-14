from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from .models import Post, Resource, ResourceLink

class PostsView(ListView):
    queryset = Post.objects.all().order_by("-created_at")
    template_name = "posts/post_list.html"
    paginate_by = 4

class HomeView(TemplateView):
    template_name = 'posts/index.html'

def post_detail(request, pk):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=pk)
    
    return render(
        request,
        "posts/post_detail.html",
        {"post": post},
    )

def rules_view(request):
    return render(request, 
    'posts/rules.html')

def resources(request):
    resources = Resource.objects.all()
    links = ResourceLink.objects.all()
    
    return render(
    request,
    'posts/resources.html',
    {'resources': resources,
    'links': links
    },
)
