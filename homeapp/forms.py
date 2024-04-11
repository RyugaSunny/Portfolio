# forms.py
from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
