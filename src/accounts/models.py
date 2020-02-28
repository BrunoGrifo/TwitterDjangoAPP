from django.db import models
from django.conf import settings
# Create your models here.

class UserProfile(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile',on_delete=models.CASCADE)
    following   = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_by')

    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        users = self.following.all()
        return users.exclude(username = self.user.username)