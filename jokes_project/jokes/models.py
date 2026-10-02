from django.contrib.auth.models import User
from django.db import models


class Joke(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jokes")
    question = models.CharField(max_length=200)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.question
