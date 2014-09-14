from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class Registration_Form(ModelForm):
	email      = forms.EmailField()
	password   = forms.CharField(), widget=forms.PasswordInput(render_value=False))
	
