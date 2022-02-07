from django import forms
from django.forms import ModelForm

from booking_form.models import Booking
from validators.form_validators import clean_name, clean_number, clean_email, clean_date


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name',
        'class': 'u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle u-white',
        'id': "name-31f5",
        'type': "text",
        'name': "name",
    }), validators=[clean_name])
    number = forms.CharField(max_length=13, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your phone number',
        'class': 'u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle u-white',
        'id': "name-31f5",
        'type': "text",
        'name': "name",
    }), validators=[clean_number])
    email = forms.CharField(widget=forms.TextInput(attrs={
        'type': "email",
        'placeholder': "Enter a valid email address",
        "id": "email-31f5",
        "name": "email",
        "class": "u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle u-white"
    }), validators=[clean_email])
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        "placeholder": "Enter your message",
        "rows": "4",
        "cols": "50",
        "id": "message-31f5",
        "name": "message",
        "class": "u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle u-white",
        "required": "",
    }))
    date = forms.DateField(widget=DateInput(attrs={
        "type": "date",
        "placeholder": "MM/DD/YYYY",
        "id": "date-f650",
        "name": "date",
        "class": "u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle u-white",
    }), validators=[clean_date])

    class Meta:
        model = Booking
        fields = [
            'name',
            'number',
            'email',
            'date',
            'time',
            'message',
        ]
        TIME_CHOICES = (
            ('', 'Preferred time'),
            ('09:00:00', '09:00'),
            ('10:00:00', '10:00'),
            ('11:00:00', '11:00'),
            ('12:00:00', '12:00'),
            ('13:00:00', '13:00'),
            ('14:00:00', '14:00'),
            ('15:00:00', '15:00'),
            ('16:00:00', '16:00'),
            ('17:00:00', '17:00'),
            ('18:00:00', '18:00'),
            ('19:00:00', '19:00'),
        )
        widgets = {
            # 'date': ,
            'time': forms.Select(choices=TIME_CHOICES, attrs={
                "type": "text",
                "id": "text-3c7c",
                "name": "text",
                "class": "u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle u-white",
            }),
        }
