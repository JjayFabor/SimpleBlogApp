from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, help_text="Excerpt of the post...")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Like by {self.user} on {self.post}"
