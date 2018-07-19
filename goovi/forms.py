from django import forms
from .models import goovi_db
class goovi_form(forms.Form):
    name = forms.CharField(max_length=50)
    file = forms.ImageField()
