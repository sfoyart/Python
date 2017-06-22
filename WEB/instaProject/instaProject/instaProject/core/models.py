from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.


def get_image_path(instance, filename):
    return(os.path.join('photos'), str(instance.id), filename)


class UserProfile(models.Model):
    user = model.ForeignKey(User, unique=True, related_name='user')
    profile_picture = ImageField(
        upload_to='media', blank=True, null=True)
    follows = models.ManyToMany(
        "self", related_name='follows', symmetrical=False)
    followed_by = models.ManyToMany(
        "self", related_name='followed_by', symmetrical=False)
