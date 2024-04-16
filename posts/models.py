from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Tag(models.Model):
    """
    Model to represent a tag.

    """

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        """Return a string representation of the object (the tag's name)."""

        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = CloudinaryField('image', blank=True, null=True)
    age = models.IntegerField(choices=[(0, '0-2 years'), (1, '2-4 years'), (2, 'Above 4 years'), (3, 'Teenagers')], default=0)
    tags = models.CharField(max_length=200, default="gentle parenting")
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    categories = models.CharField(max_length=100, choices=[
        ("Feeding & Nutrition", "Feeding & Nutrition"),
        ("Health Concerns", "Health Concerns"),
        ("Toys & Activities", "Toys & Activities"),
        ("Breastfeeding", "Breastfeeding"),
        ("Parental Separation", "Parental Separation"),
        ("Home Organization", "Home Organization"),
        ("Sleeping Patterns", "Sleeping Patterns"),
        ("Behavioural Issues", "Behavioural Issues"),
        ("Gentle Parenting", "Gentle Parenting"),
    ], default="Feeding & Nutrition")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} | {self.author}"

    def save(self, *args, **kwargs):
        if self.tags:
            self.tags = ','.join(['#' + tag.strip() for tag in self.tags.split(',')])
        super(Post, self).save(*args, **kwargs)

    def user_has_liked(self, user):
        return self.likes.filter(id=user.id).exists()

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = CloudinaryField('image', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

    def edit_comment(self, new_content):
        self.content = new_content
        self.save()

    def delete_comment(self):
        self.delete()

    class Meta:
        ordering = ["-created_at"]


class Resource(models.Model):
    name = models.CharField(max_length=100)
    file = CloudinaryField('file')
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name


class ResourceLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class ContactRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"
