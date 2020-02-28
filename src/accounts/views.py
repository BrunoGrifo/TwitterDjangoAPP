from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

class UserDetailView(View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, username__iexact=self.kwargs.get("username"))
        print(user.username)
        context = {
            'user': user
        }
        return render(request, 'accounts/user_details.html', context)

