from django.db import models
from django.contrib.auth.models import User


class Paste(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)
    unique_url = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.title} ({'Private' if self.is_private else 'Public'})"