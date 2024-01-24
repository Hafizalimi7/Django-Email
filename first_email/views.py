from django.shortcuts import render
from django.views.generic import FormView, TemplateView
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
    return super(UserView, self).form_valid(form)
  

class EmailSent(TemplateView):
  template_name = 'success.html'
  def get(self, request):
    author = UserEmail.objects.get(author)
    print(author)
    return render(request, 'success.html', context={'authors': author})

  
 