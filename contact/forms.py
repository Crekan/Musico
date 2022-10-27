from django.forms import ModelForm, Textarea, EmailInput, CharField
from .models import *


class GetInTouchForm(ModelForm):
    # email = EmailInput
    class Meta:
        model = GetInTouch
        fields = ('text', 'name', 'get_in_touch_email', 'subject')

        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control w-100',
                'cols': '30',
                'rows': '9',
                'placeholder': 'Enter Message'
            }),
            'name': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
                'rows': '2'
            }),
            'get_in_touch_email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address',
                'rows': '2',
            }),
            'subject': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Subject',
                'rows': '2'
            }),
        }
