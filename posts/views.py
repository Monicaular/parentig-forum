from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Post, Resource, ResourceLink, Comment, Rule
from .forms import PostForm, ContactForm, CommentForm
from django.db.models import Q


class PostsView(ListView):
    """
    A view that lists all posts, ordered by creation date in descending order. It supports pagination,
    filtering by age and category, and keyword search.

    Attributes:
        queryset (QuerySet): Initial queryset of Post objects.
        template_name (str): The path to the template used for rendering the posts.
        paginate_by (int): Number of posts displayed per page.
    """

    queryset = Post.objects.all().order_by("-created_at")
    template_name = "posts/post_list.html"
    paginate_by = 4

    def get_queryset(self):
        """
        Extends the base queryset with filtering capabilities based on the request's GET parameters.

        Returns:
            QuerySet: The filtered queryset based on age, category, and search query.
        """
        queryset = Post.objects.all().order_by("-created_at")
        filtered = False

        # Filtering by age
        age = self.request.GET.get("age")
        if age:
            queryset = queryset.filter(age=age)
            filtered = True

        # Filtering by category
        category = self.request.GET.get("category")
        if category:
            queryset = queryset.filter(categories=category)
            filtered = True

        # Searching by keyword
        search_query = self.request.GET.get("search_query")
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
                | Q(content__icontains=search_query)
                | Q(tags__icontains=search_query)
            )

            filtered = True

        if not queryset.exists():
            if search_query:
                messages.info(
                    self.request,
                    "No posts found matching your search criteria.",
                    extra_tags="filter-message",
                )
            elif filtered:
                messages.info(
                    self.request,
                    "No posts found matching your filter criteria.",
                    extra_tags="filter-message",
                )
            else:
                messages.info(
                    self.request, "No posts available.", extra_tags="filter-message"
                )

        return queryset


class HomeView(ListView):
    """
    Home page view that lists featured posts, limited to the five most recent ones.

    Attributes:
        template_name (str): Specifies the path to the template used for rendering the home page.
        context_object_name (str): Name of the context object used to return the queryset in the template.
    """

    template_name = "posts/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        """
        Retrieves the top five featured posts ordered by their creation date in descending order.

        Returns:
            QuerySet: The queryset of the top five featured posts.
        """
        return Post.objects.filter(is_featured=True).order_by("-created_at")[:6]


@login_required
def post_detail(request, pk):
    """
    A view that displays a detailed page for a specific post by primary key (pk). It includes comments and a form to submit a comment.
    If a POST request is made, it processes the submitted comment form.

    Parameters:
        request (HttpRequest): The request object used to generate the response.
        pk (int): The primary key of the Post object to retrieve.

    Template:
        posts/post_detail.html

    Returns:
        HttpResponse: A response object containing the rendered template.
    """
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
            messages.success(request, "Your comment has been posted successfully!")

            url = reverse("post_detail", args=[pk]) + f"#comment{comment.id}"
            return redirect(url)
        else:
            for error in comment_form.errors:
                messages.error(request, f"{error}")
    else:
        comment_form = CommentForm()

    return render(
        request,
        "posts/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


@login_required
def create_post(request):
    """
    View for creating a new post. Handles both GET and POST requests. If the request is POST,
    it attempts to save the new post based on the form data. Redirects to the post detail page
    upon successful post creation.

    Parameters:
        request (HttpRequest): The request object used to generate this response.

    Template:
        posts/create_post.html

    Returns:
        HttpResponse: A response object containing the rendered template on GET or
                      a redirect on successful POST.
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your post has been submitted successfully!")
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "posts/create_post.html", {"form": form})


@login_required
def edit_post(request, pk):
    """
    Allows a user to edit an existing post, identified by its primary key (pk).
    Redirects to the post detail page upon successful update or back to the edit
    form if validation fails.

    Parameters:
        request (HttpRequest): The request object used to generate this response.
        pk (int): The primary key of the Post to edit.

    Template:
        posts/edit_post.html

    Returns:
        HttpResponse: Redirects to the post detail page on successful update or
                      renders the edit form again with error messages on failure.
    """
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect("post_detail", pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Your post has been updated successfully!")
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "posts/edit_post.html", {"form": form, "post": post})


@login_required
def delete_post(request, pk):
    """
    Deletes a post identified by its primary key (pk) upon POST request. Users are only allowed
    to delete their own posts. Redirects to the post list after deletion.

    Parameters:
        request (HttpRequest): The request object used to generate this response.
        pk (int): The primary key of the Post to delete.

    Returns:
        HttpResponseRedirect: Redirects to the post list view after deletion or back to the post detail
                             view if not a POST request.
    """
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Your post has been succesfully deleted!")

        return redirect("post_list")
    return redirect("post_detail", pk=pk)


@login_required
def like_post(request, post_id):
    """
    Allows a user to like or unlike a post identified by its post_id. This view toggles the like status:
    if the user has already liked the post, it removes their like; otherwise, it adds a like from the user.

    Parameters:
        request (HttpRequest): The request object used to generate this response.
        post_id (int): The ID of the Post to like or unlike.

    Returns:
        HttpResponseRedirect: Redirects to the post detail view of the liked or unliked post.
    """
    post = Post.objects.get(id=post_id)
    if request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, "You unliked this post!")
        else:
            post.likes.add(request.user)
            messages.success(request, "You liked this post!")
    return redirect("post_detail", pk=post_id)


@login_required
def edit_comment(request, pk, comment_id):
    """
    Allows a user to edit an existing comment, identified by its primary key (comment_id),
    on a post identified by its primary key (pk).

    Parameters:
        request (HttpRequest): The request object used to generate the response.
        pk (int): The primary key of the Post associated with the comment.
        comment_id (int): The primary key of the Comment to edit.

    Returns:
        HttpResponseRedirect: Redirects to the post detail page after the comment is edited or in case of form errors.
    """
    post = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect("post_detail", pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully!")
            return redirect("post_detail", pk=pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, "posts/edit_comment.html", {"form": form, "post": post})


@login_required
def delete_comment(request, pk, comment_id):
    """
    Allows the author of a comment to delete their own comment.
    Ensures that users can only delete comments they authored.

    Parameters:
        request (HttpRequest): The request object used to generate this response.
        pk (int): The primary key of the Post that the comment is associated with.
        comment_id (int): The primary key of the Comment to delete.

    Returns:
        HttpResponseRedirect: Redirects to the post detail view after deleting
        the comment or displays an error message if the user is not authorized to delete the comment.
    """
    post = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
    else:
        messages.error(request, "You can only delete your own comments!")

    return redirect("post_detail", pk=pk)


@login_required
def like_comment(request, comment_id):
    """
    Allows a user to like or unlike a comment identified by its comment_id. This view toggles the like status:
    if the user has already liked the comment, it removes their like; otherwise, it adds a like from the user.

    Parameters:
        request (HttpRequest): The request object used to generate this response.
        comment_id (int): The ID of the Comment to like or unlike.

    Returns:
        HttpResponseRedirect: Redirects to the post detail view of the post associated with the commented,
                             allowing the user to see the updated like status.
    """
    comment = Comment.objects.get(id=comment_id)
    if request.user.is_authenticated:
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
            messages.success(request, "You unliked this comment!")
        else:
            comment.likes.add(request.user)
            messages.success(request, "You liked this comment!")
    else:
        messages.error(request, "Please log in to like comments.")
    return redirect("post_detail", pk=comment.post.pk)


def rules_view(request):
    """
    Displays the forum rules retrieved from the Rule model.

    Parameters:
        request (HttpRequest): The request object used to generate this response.

    Template:
        posts/rules.html

    Returns:
        HttpResponse: Renders the rules template with the list of all forum rules.
    """
    rules = Rule.objects.all()
    return render(request, "posts/rules.html", {"rules": rules})


def resources(request):
    """
    Displays available resources and links to external resources. Retrieves all resources
    from the Resource model and resource links from the ResourceLink model.

    Parameters:
        request (HttpRequest): The request object used to generate this response.

    Template:
        posts/resources.html

    Returns:
        HttpResponse: Renders the resources template with the list of resources and resource links.
    """
    resources = Resource.objects.all()
    links = ResourceLink.objects.all()

    return render(
        request,
        "posts/resources.html",
        {"resources": resources, "links": links},
    )


def contact_us(request):
    """
    Handles the contact form submissions. On POST, validates and saves the contact form data.
    Notifies the user of the form submission status and redirects to the contact page.

    Parameters:
        request (HttpRequest): The request object used to generate this response.

    Template:
        posts/contact.html

    Returns:
        HttpResponse: Redirects to the contact page after form submission or renders the contact form on GET.
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request, "Your contact request has been submitted successfully!"
            )
            return redirect("contact")
    else:
        contact_form = ContactForm()

    return render(
        request,
        "posts/contact.html",
        {"contact_form": contact_form},
    )

