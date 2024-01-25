from typing import Any
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, DetailView, ListView
from .forms import InputForm
from .models import UserEmail
from django.urls import reverse_lazy


# Create your views here.

class HomeView(TemplateView):
  template_name = "base.html"
  
class UserView(FormView):
  template_name = "email.html"
  form_class = InputForm
  
  success_url = reverse_lazy('success')
  
  def form_valid(self, form):
    form.save()
    pk_value = form.instance.pk
    self.success_url = reverse_lazy('success', kwargs={'pk': pk_value})
    return super(UserView, self).form_valid(form)


class EmailSent(DetailView):
  template_name = 'success.html'
  model = UserEmail


class AllEmails(ListView):
  model = UserEmail
  template_name = 'allmail.html'
  context_object_name = 'all_emails'
  ordering = ['-date']
 

  
 