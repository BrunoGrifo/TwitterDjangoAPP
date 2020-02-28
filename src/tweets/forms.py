from django.db import models
from django import forms

from .models import Tweet


class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder':"Your tweet", 'class':"form-control"}))
    class Meta:
        model = Tweet
        fields = ["content"]
    
    # def clean_content(self, *args, **kwargs):
    #     content = self.cleaned_data['content']
    #     if any(word in content.lower() for word in curse_words):
    #         raise forms.ValidationError("YOOOOO don't swear")
    #     return content