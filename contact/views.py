from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from telebot.sendmessage import sendTelegram

from .forms import *


class ContactFormView(FormView):
    form_class = GetInTouchForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact')

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        text = request.POST['text']
        sendTelegram(tg_name=name, tg_text=text)
        return redirect('contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Locate.objects.all()
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('contact')
