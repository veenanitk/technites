from django import forms
from django.core import validators
from polls.models import paste
from django.db import models



class input(forms.ModelForm):
    
    class Meta:
        model = paste
        fields= '__all__'