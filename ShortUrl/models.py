from django.db import models


class ShortenedLink(models.Model):
    original_url = models.URLField(max_length=200)
    shortened_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_url} with code : {self.shortened_code}"