from django.db import models
from django.contrib.auth.models import User


class ShortUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    base_url = models.URLField()
    short_url = models.URLField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.base_url
