from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    email = forms.CharField(max_length=200, required=True, label='email')
    author = forms.CharField(max_length=40, required=True, label='Author')
    text = forms.CharField(max_length=3000, required=True, label='Text',widget=widgets.Textarea)