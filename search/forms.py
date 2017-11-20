from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='your name', max_length=100)
    groups = forms.CharField(label='groups', max_length=1000)

class Login(forms.Form):
    at = forms.CharField(label = 'at', max_length=1000)
