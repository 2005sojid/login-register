from django.urls import reverse
from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
