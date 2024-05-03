from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Tag(models.Model):
    """
    Represents a tag that can be applied to posts. Tags help in categorizing content
    into different topics which makes it easier for users to find related content.
    
    Attributes:
        name (CharField): The name of the tag. Must be unique.
    """
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        """Return a string representation of the tag."""

        return str(self.name)

class Post(models.Model):
    """
    Represents a blog post in the forum. Posts can be tagged, liked, and categorized.
    
    Attributes:
        title (CharField): The title of the post.
        content (TextField): The full text content of the post.
        author (ForeignKey): The user who authored the post.
        created_at (DateTimeField): The date and time the post was created.
        updated_at (DateTimeField): The date and time the post was last updated.
        is_featured (BooleanField): True if the post is featured on the site.
        photo (CloudinaryField): An optional image for the post.
        age (IntegerField): Categorized age group for the post audience.
        tags (CharField): Comma-separated tags for the post.
        likes (ManyToManyField): Users who have liked the post.
        categories (CharField): The category of the post.
    """
    # model fields
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
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
        """
        Return a string representation of the post,
        showing title and author.
        """
        return f"{self.title} | {self.author}"

    def save(self, *args, **kwargs):
        """
        Overriding the save method to add a hash (#) before each tag in the tags string.
        """
        if self.tags:
            self.tags = ','.join(['#' + tag.strip() for tag in self.tags.split(',')])
        super(Post, self).save(*args, **kwargs)

    def user_has_liked(self, user):
        return self.likes.filter(id=user.id).exists()

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Represents a comment made on a post. Comments allow users to engage with the content.
    
    Attributes:
        post (ForeignKey): The post to which the comment is associated.
        author (ForeignKey): The user who authored the comment.
        content (TextField): The text content of the comment.
        created_at (DateTimeField): The date and time the comment was created.
        updated_at (DateTimeField): The date and time the comment was last updated.
        photo (CloudinaryField): An optional image for the comment.
        likes (ManyToManyField): Users who have liked the comment.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = CloudinaryField('image', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)

    def __str__(self):
        """
        Return a string representation of the comment,
        showing the author and the post title.
        """
        return f"Comment by {self.author.username} on {self.post.title}"

    def edit_comment(self, new_content):
        self.content = new_content
        self.save()

    def delete_comment(self):
        self.delete()

    class Meta:
        ordering = ["-created_at"]

class Rule(models.Model):
    """
    Represents a community rule. Rules are important for setting expectations and guidelines for community behavior.
    
    Attributes:
        title (CharField): The title of the rule.
        description (TextField): A detailed description of what the rule entails.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """
        Return a string representation of the rule,
        showing its title.
        """
        return self.title
        

class Resource(models.Model):
    """
    Represents a resource such as a document or file that provides valuable information.
    
    Attributes:
        name (CharField): The name of the resource.
        file (CloudinaryField): The file associated with the resource.
        description (TextField): A brief description of the resource.
        image (CloudinaryField): An optional image for the resource.
    """
    name = models.CharField(max_length=100)
    file = CloudinaryField('file')
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        """Return a string representation of the resource."""
        return self.name


class ResourceLink(models.Model):
    """
    Represents a link to an external resource. Useful for linking to additional information or related sites.
    
    Attributes:
        name (CharField): The display name of the link.
        url (URLField): The URL to the external resource.
    """
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        """Return a string representation of the resource link."""
        return self.name

class ContactRequest(models.Model):
    """
    Represents a contact request sent by a user. Used for users to send messages to the site administrators.
    
    Attributes:
        name (CharField): The name of the person sending the contact request.
        email (EmailField): The email address of the sender.
        message (TextField): The content of the message.
        read (BooleanField): Whether the message has been read by an administrator.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """
        Return a string representation of the contact request, showing the sender's name.
        """
        return f"Message from {self.name}"
