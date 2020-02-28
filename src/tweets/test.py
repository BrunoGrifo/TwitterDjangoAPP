from django.test import TestCase
from django.urls import reverse
from .models import Tweet
from django.contrib.auth import get_user_model

User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="Eduardo")
    
    def test_tweet(self):
        obj=Tweet.objects.create(
            user=User.objects.first(),
            content="test case yoyo"
        )
        self.assertTrue(obj.content == "test case yoyo")
        absolute_url = reverse("tweets:TweetDetailView", kwargs={"pk":1})
        self.assertTrue(obj.get_absolute_url(), absolute_url)
    
    def test_tweet_url(self):
        obj=Tweet.objects.create(
            user=User.objects.first(),
            content="test case yoyo"
        )
        self.assertTrue(obj.content == "test case yoyo")
        absolute_url = reverse("tweets:TweetDetailView", kwargs={"pk":obj.pk})
        self.assertTrue(obj.get_absolute_url(), absolute_url)