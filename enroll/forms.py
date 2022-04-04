from tkinter import Widget
from django.core import validators
from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','number','image']
        Widget={
            'name':forms.TextInput(attrs={'class':'form-control my-3','placeholder':'Enter name'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'number':forms.NumberInput(attrs={'class':'form-control'}), 
            
        }
    