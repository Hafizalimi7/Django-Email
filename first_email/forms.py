from django import forms
from .models import UserEmail
# creating a form 
class InputForm(forms.ModelForm):
   class Meta:
     model = UserEmail
     fields = "__all__"
  
