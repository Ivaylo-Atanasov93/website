from django import forms
from django.forms import ModelForm

from contacts.models import ContactMe
from validators.form_validators import clean_name, clean_surname, clean_email


class ContactMeForm(ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'class': 'form-control',
    }), validators=[clean_name])
    surname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Your surname',
        'class': 'form-control',
    }), validators=[clean_surname])
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email',
        'class': 'form-control',
    }), validators=[clean_email])
    message = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={
        'placeholder': 'Your message',
        'class': 'form-control',
    }))

    class Meta:
        model = ContactMe
        fields = [
            'name',
            'surname',
            'email',
            'message',
        ]
