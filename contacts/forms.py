from django import forms
from django.forms import ModelForm

from contacts.models import ContactMe
from validators.form_validators import clean_name, clean_email


class ContactMeForm(ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "type": "text",
        "placeholder": "Enter your Name",
        "id": "name-da97",
        "name": "name",
        "class": "u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-grey-5 u-input u-input-rectangle",  # noqa
        "required": "",
    }), validators=[clean_name])
    email = forms.CharField(widget=forms.TextInput(attrs={
        "type": "email",
        "placeholder": "Enter a valid email address",
        "id": "email-da97",
        "name": "email",
        "class": "u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-grey-5 u-input u-input-rectangle",
        "required": "",
    }), validators=[clean_email])
    message = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={
        "placeholder": "Enter your message",
        "rows": "4",
        "cols": "50",
        "id": "message-da97",
        "name": "message",
        "class": "u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-grey-5 u-input u-input-rectangle",
        "required": "",
    }))

    class Meta:
        model = ContactMe
        fields = [
            'name',
            'email',
            'message',
        ]
