from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
