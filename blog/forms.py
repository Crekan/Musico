from django import forms
from django.forms import ModelForm, TextInput

from .models import *


class CommentForm(ModelForm):
    class Meta:
        model = CommentPost
        fields = ('text', 'email')

        widgets = {
            'text': TextInput(attrs={
                'class': 'form-control w-100 col-12',
                'placeholder': 'Write Comment'
            }),
            'email': TextInput(attrs={
                'class': 'form-control col-sm-12',
                'type': 'email',
                'placeholder': 'Email'
            }),
        }
