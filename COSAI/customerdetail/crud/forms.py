from django import forms  
from crud.models import *
from django.forms import fields

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Uploadedfiles 
        fields = [
           'uploads1', 
        ]