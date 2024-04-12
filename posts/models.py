from django.db import models
from django.contrib.auth.models import User

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
    photo = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    age = models.IntegerField(choices=[(0, '0-2 years'), (1, '2-4 years'), (2, 'Above 4 years')], default=0)
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    categories = models.CharField(max_length=100, choices=[
        ("Feeding & Nutrition", "Feeding & Nutrition"),
        ("Health Concerns", "Health Concerns"),
        ("Toys & Activities", "Toys & Activities"),
        ("Breastfeeding", "Breastfeeding"),
        ("Parental Separation", "Parental Separation"),
        ("Home Organization", "Home Organization"),
    ], default="Feeding & Nutrition")

    def __str__(self):
        return self.title


