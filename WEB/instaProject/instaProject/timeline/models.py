import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    description = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, related_name='author')
    picture = models.ImageField(upload_to='img/all-images', null=True)
    pub_date = models.DateTimeField('date published',  auto_now_add=True)

    def __str__(self):
        return self.description

    def was_published_recently(self):
        return timezone.now() <= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
