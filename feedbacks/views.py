#-*-coding: utf-8-*-
from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.mail import send_mass_mail, send_mail
from feedbacks.models import Feedback
from feedbacks.forms import *
from django.conf import settings

class FeedbackView(CreateView):
    model = Feedback
    fields = ['name','subject','message','from_email','create_date']
    template_name = 'feedbacks/feedback.html'
    success_url = reverse_lazy('feedback')
    def form_valid(self, form):
        send_mail(form.cleaned_data['subject'], form.cleaned_data['message'], form.cleaned_data['from_email'], settings.ADMINS, fail_silently=False)
        messages.success(self.request, u'Thank you for your feedback! We will keep in touch with you very soon!')
        return super(FeedbackView, self).form_valid(form)
