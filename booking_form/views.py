from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView

from booking_form.forms import BookingForm
from booking_form.models import Booking


# # Create your views here.

class BookingCreateView(CreateView):
    template_name = 'booking_page.html'
    form_class = BookingForm
    queryset = Booking.objects.all()

    def form_valid(self, form):

        name = form.cleaned_data.get('name')
        surname = form.cleaned_data.get('surname')
        number = form.cleaned_data.get('number')
        email = form.cleaned_data.get('email')
        date = form.cleaned_data.get('date')
        time = form.cleaned_data.get('time')
        customers_message = form.cleaned_data.get('message')
        message = f'Message from {name} {surname}\n\n'
        message += f'The lesson is booked on {date} at {time}\n'
        message += f'\n\n{customers_message}\n\n'
        message += f'Contacts:\n\nPhone: {number}\nE-mail: {email}'
        send_mail(
            subject=f'New booked lesson from {name} {surname}!',
            message=message,
            from_email='dimitar.kanchev1993@gmail.com',
            recipient_list=[email, 'dimitar.kanchev1993@abv.bg'],
        )

        return super().form_valid(form)


class BookingView(DetailView):
    template_name = 'created_booking.html'
    queryset = Booking.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Booking, id=id_)
