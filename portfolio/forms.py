from django import forms 
from portfolio.models import Contact
from django.core import validators


class NewContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'