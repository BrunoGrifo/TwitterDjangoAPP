from django.db import models
from django.conf import settings
from django.urls import reverse
import datetime

from .validators import *

    


# class TweetObjects(models.Manager):
#     def get_queryset(self):
#         tweets = super(TweetObjects, self).get_queryset().all()
#         return tweets


# class TweetDateOrder(models.Manager):
#     def get_queryset(self):
#         tweets = super(TweetDateOrder, self).get_queryset().all().order_by('-timestamp')
#         return tweets


# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140, validators=[validate_content])
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # objects=TweetObjects()
    # order_by_date=TweetDateOrder()
    
    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return str(self.content)
    
    # def clean(self, *ar gs, **kwargs):
    #     content = self.content
    #     if any(word in content.lower() for word in curse_words):
    #         raise ValidationError("YOOOOO don't swear")
    #     return super(Tweet, self).clean(self, *args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("tweets:TweetDetailView", kwargs={"pk":self.pk})