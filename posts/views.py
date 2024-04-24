from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Post, Resource, ResourceLink, Comment, Rule
from .forms import PostForm, ContactForm, CommentForm
from django.db.models import Q


class PostsView(ListView):
    queryset = Post.objects.all().order_by("-created_at")
    template_name = "posts/post_list.html"
    paginate_by = 4

    def get_queryset(self):
        queryset = Post.objects.all().order_by("-created_at")

        # Filtering by age
        age = self.request.GET.get('age')
        if age:
            queryset = queryset.filter(age=age)

        # Filtering by category
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(categories=category)

        # Searching by keyword
        search_query = self.request.GET.get('search_query')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(content__icontains=search_query) | 
                Q(tags__icontains=search_query)
            )

        return queryset

class HomeView(TemplateView):
    template_name = 'posts/index.html'

def post_detail(request, pk):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=pk)
    comments = post.comments.all().order_by("-created_at")
    comment_count = post.comments.count()

    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            comment_form = CommentForm()
            messages.success(request, 'Your comment has been posted successfully!', extra_tags='comment')

            url = reverse('post_detail', args=[pk]) + f'#comment{comment.id}'
            return redirect(url)
        else:
            for error in comment_form.errors:
                messages.error(request, f'{error}', extra_tags='comment')
    else:
        comment_form = CommentForm()

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
            messages.add_message(request, messages.INFO, "You unliked this!", extra_tags='like-post')
        else:
            post.likes.add(request.user)
            messages.add_message(request, messages.INFO, "You liked this!", extra_tags='like-post')
    return redirect('post_detail', pk=post_id)


def edit_comment(request, pk, comment_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        queryset = post.comments.all()
        comment = get_object_or_404(queryset, pk=comment_id)

        if comment.author == request.user:
            comment_form = CommentForm(request.POST, instance=comment)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                messages.success(request, "Comment updated successfully!", extra_tags='comment')
            else:
                messages.error(request, "Error updating comment", extra_tags='comment')
        else:
            messages.error(request, "You are not authorized to edit this comment.", extra_tags='comment')

    return HttpResponseRedirect(reverse('post_detail', kwargs={'pk': pk}))


def delete_comment(request, pk, comment_id):
    """
    View to delete comment
    """
    post = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully!', extra_tags='comment')
    else:
        messages.error(request, 'You can only delete your own comments!', extra_tags='comment')

    return redirect('post_detail', pk=pk)


def like_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user.is_authenticated:
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
            messages.success(request, "You unliked this comment!", extra_tags='like-comm')
        else:
            comment.likes.add(request.user)
            messages.success(request, "You liked this comment!", extra_tags='like-comm')
    else:
        messages.error(request, "Please log in to like comments.", extra_tags='like-comm')
    return redirect('post_detail', pk=comment.post.pk)


def rules_view(request):
    rules = Rule.objects.all()
    return render(request,
    'posts/rules.html',
    {'rules': rules
    }
)

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
            messages.success(request, "Your contact request has been submitted successfully!", extra_tags='contact')
            return redirect('contact')
    else:
        contact_form = ContactForm()

    return render(
        request,
        "posts/contact.html",
        {'contact_form': contact_form },
    )