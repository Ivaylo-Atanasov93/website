from django import forms
from django.forms import ModelForm

from booking_form.models import Booking
from validators.form_validators import clean_name, clean_surname, clean_number, clean_email, clean_date


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'class': 'form-control',
    }), validators=[clean_name])
    surname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Your surname',
        'class': 'form-control',
    }), validators=[clean_surname])
    number = forms.CharField(max_length=13, widget=forms.TextInput(attrs={
        'placeholder': '07 123 456 789',
        'class': 'form-control',
    }), validators=[clean_number])
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email',
        'class': 'form-control',
    }), validators=[clean_email])
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        'placeholder': 'Your message',
        'class': 'form-control',
    }))
    date = forms.DateField(widget=DateInput(attrs={'class': 'form-control', 'placeholder': 'Preferred date'}), validators=[clean_date])

    class Meta:
        model = Booking
        fields = [
            'name',
            'surname',
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
            'time': forms.Select(choices=TIME_CHOICES, attrs={'class': 'form-control'}),
        }
