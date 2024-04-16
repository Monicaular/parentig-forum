from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from django.contrib import messages
from .models import Post, Resource, ResourceLink
from .forms import PostForm, ContactForm, CommentForm

class PostsView(ListView):
    queryset = Post.objects.all().order_by("-created_at")
    template_name = "posts/post_list.html"
    paginate_by = 4


class HomeView(TemplateView):
    template_name = 'posts/index.html'

def post_detail(request, pk):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=pk)
    comments = post.comments.all().order_by("-created_at")
    comment_count = post.comments.count()

    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            comment_form = CommentForm()
            messages.success(request, 'Your comment has been posted successfully!')
            return redirect(request.path)
        else:
            messages.error(request, 'There was an error posting your comment. Please try again.')

    return render(
        request,
        "posts/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return redirect('post_detail', pk=pk)


def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.add_message(request, messages.INFO, "You unliked this!")
        else:
            post.likes.add(request.user)
            messages.add_message(request, messages.INFO, "You liked this!")
    return redirect('post_detail', pk=post_id)

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

def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Your contact request has been submitted successfully!")
            return redirect('contact')
    else:
        contact_form = ContactForm()

    return render(
        request,
        "posts/contact.html",
        {'contact_form': contact_form },
    )