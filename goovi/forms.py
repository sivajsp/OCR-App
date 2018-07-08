from django import forms
class goovi_form(forms.Form):
    name = forms.CharField(max_length=50)
    file = forms.ImageField()
