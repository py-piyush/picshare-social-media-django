from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="images_created",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000, blank=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="images_liked", blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("images:detail", args=[self.id, self.slug])

    class Meta:
        indexes = [
            models.Index(fields=["-created"]),
        ]

        ordering = ["-created"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="commented", on_delete=models.CASCADE
    )
    post = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
