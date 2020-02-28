from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django import forms
from django.forms.utils import ErrorList

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.views.decorators.csrf import requires_csrf_token
from .json import JsonResponseAjaxSuccess, JsonResponseBadRequest
from django.http import JsonResponse

from .models import *
from .forms import *

# Global variables


# ---------------------------------------------------------                Create              ---------------------------------------------------------

class TweetCreateView(FormUserNeededMixin , CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # login_url = '/admin/'
    # redirect_field_name = 'tweetCreateView'
    # success_url="/tweets/"

    # -- -- -- -- -- -- -- -- -- -- -- -- --GET and POST-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --      
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid(): 
    #         form.instance.user = self.request.user
    #         return HttpResponseRedirect(reverse('tweets:tweet_list_view'), {'tweet_list': querySet})
    #     else:
    #         return render(request, self.template_name, {'form':form}) 

    # WITHOUT MIXIN
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid(): 
    #         if self.request.user.is_authenticated:
    #             form.instance.user = self.request.user
    #             return HttpResponseRedirect(reverse('tweets:tweet_list_view'), {'tweet_list': querySet})
    #         else:
    #             form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])        
    #     return render(request, self.template_name, {'form':form}) 
    
    # def get(self, request, *args, **kwargs):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})
    #-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    
# - - - - - - - FUNCTION BASED VIEWS- - - - - - - - - - - - - - - - - - - - - - - - - - 

# def tweetCreateView(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         if request.user.is_authenticated :
#             instance = form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#         else:
#             form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
#     context = {
#         'form': form
#     }
#     return render(request, 'tweets/create_view.html', context) 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# ---------------------------------------------------------                Retrieve               ---------------------------------------------------------


class tweet_list_view(View):
    http_method_names =['get']
    
    def get(self, request):
        # tweets = Tweet.sorted_by_date.all()
        tweets = Tweet.objects.all()
        query = self.request.GET.get("q",None)
        if query is not None:
            tweets = tweets.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        context = {
            "tweet_list": tweets,
            "create_form": TweetModelForm(),
            "action_url": reverse('tweets:tweetCreateView'),
        }
        return render(request, 'tweets/list_view.html', context) 
    

class TweetDetailView(View):
    http_method_names =['get']

    def get(self, request, pk):
        tweet = get_object_or_404(Tweet, pk=pk)
        context = {
            'tweet': tweet
        }
        return render(request, 'tweets/detail_view.html', context)
 


# ---------------------------------------------------------                Update              ---------------------------------------------------------

class TweetUpdateView(UserOwnerMixin,UpdateView):
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = '/tweets/'

    def get_queryset(self) :
        queryset = Tweet.objects.all()
        return queryset
 
# ---------------------------------------------------------                Delete              ---------------------------------------------------------

# class TweetDeleteView(LoginRequiredMixin, DeleteView):
#     model = Tweet
#     template_name = "tweets/delete_view.html"
#     success_url = reverse_lazy("tweets:tweet_list_view")

class TweetDeleteView(View):
    http_method_names = ['delete']

    # def get(self, request, pk):
    #     print("yooooooooooo")
    #     tweet = get_object_or_404(Tweet, pk=pk)
    #     context = {
    #         'tweet': tweet
    #     }
    #     return render(request, 'tweets/delete_view.html', context)
   
    # def delete(self, request, pk: int):
    #     Tweet.objects.get(pk=pk).delete()
    #     tweets = Tweet.objects.all()
    #     return HttpResponseRedirect(reverse('tweets:tweet_list_view'), {"tweet_list": tweets})
    #     try:
    #         if not Tweets.objects.filter(pk=pk).exists():
    #             return JsonResponseBadRequest("Tweet não existe!")
    #         with transaction.atomic():              
    #             MaterialRequest.objects.filter(pk=mr_id).delete()
    #         return JsonResponseAjaxSuccess()
    #     except Exception as e:
    #         print(e)
    #         return JsonResponseBadRequest("Problemas a remover o Pedido de Preparação de Material!")


    def delete(self, request, pk):
        print("Entrou no delete")
        Tweet.objects.get(pk=pk).delete()
        return JsonResponse({})


    
    
    #   def delete(self, request, mr_id: int):
    #     try:
    #         if not MaterialRequest.objects.filter(pk=mr_id, state_id=OrderState.EDIT).exists():
    #             return JsonResponseBadRequest("Pedido de Preparação de Material não existe ou já está submetido!")
    #         with transaction.atomic():
    #             MaterialRequestArm.objects.filter(matreq_id=mr_id).delete()
    #             MaterialRequestAddress.objects.filter(matreq_id=mr_id).delete()
    #             MaterialRequestProduct.objects.filter(matreq_id=mr_id).delete()
    #             MaterialRequest.objects.filter(pk=mr_id).delete()
    #         return JsonResponseAjaxSuccess()
    #     except Exception as e:
    #         print(e)
    #         return JsonResponseBadRequest("Problemas a remover o Pedido de Preparação de Material!")
    
    
  
  

