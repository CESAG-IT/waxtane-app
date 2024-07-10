from django import forms
from .models import HashTag

class TagForm(forms.ModelForm):
    class Meta:
        model = HashTag
        fields = ['name']