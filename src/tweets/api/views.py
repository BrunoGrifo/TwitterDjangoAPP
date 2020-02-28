from rest_framework import generics
from rest_framework.views import APIView
from tweets.models import Tweet
from .serializers import TweetModelSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .pagination import StandardResultsSetPagination


class TweetListAPIView(generics.ListAPIView):
    serializer_class=TweetModelSerializer
    pagination_class = StandardResultsSetPagination


    def get_queryset(self, *args, **kwargs):
        # tweets = Tweet.order_by_date.all()
        tweets = Tweet.objects.all()
        query = self.request.GET.get("q",None)
        if query is not None:
            tweets = tweets.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return tweets


class TweetCreateAPIView(APIView):
    serializer_class=TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            tweet = serializer.save(user=self.request.user)
            serializer = TweetModelSerializer(tweet)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)