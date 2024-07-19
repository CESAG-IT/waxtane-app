from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'birthday']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }