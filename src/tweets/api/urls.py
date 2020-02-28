from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


from . import views

app_name="tweets-api"

urlpatterns = [
    path('', views.TweetListAPIView.as_view(), name='TweetListAPIView'),
    path('create/', views.TweetCreateAPIView.as_view(), name='TweetCreateAPIView'),
]


# if settings.DEBUG:
#     urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)) 