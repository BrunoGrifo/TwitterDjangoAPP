from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


from . import views

app_name="tweets"

urlpatterns = [
    path('', RedirectView.as_view(url="/"), name = 'list_home'),
    path('search/', views.tweet_list_view.as_view(), name = 'tweet_list_view'),
    path('create/', views.TweetCreateView.as_view(), name = 'tweetCreateView'),
    path('detail/<int:pk>/', views.TweetDetailView.as_view() , name = 'TweetDetailView'),
    path('detail/<int:pk>/edit', views.TweetUpdateView.as_view(), name = 'TweetUpdateView'),
    path('<int:pk>/delete', views.TweetDeleteView.as_view(), name = 'TweetDeleteView'), 
    
]


if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)) 