from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
# Create your views here.
from django.views.generic import CreateView, DetailView

from contacts.forms import ContactMeForm
from contacts.models import ContactMe


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactMeForm
    queryset = ContactMe.objects.all()

    def form_valid(self, form):
        # name = form.cleaned_data.get('name')
        # surname = form.cleaned_data.get('surname')
        # email = form.cleaned_data.get('email')
        # customers_message = form.cleaned_data.get('message')
        # message = f'Message from {name} {surname}\n'
        # message += f'\n\n{customers_message}'
        # message += f'Contacts:\nE-mail: {email}'
        # send_mail(
        #     subject=f'New booked lesson from {name} {surname}!',
        #     message=message,
        #     from_email='contact-form@myapp.com',
        #     recipient_list=[email, '@owners_email'],
        # )

        return super().form_valid(form)


class ContactView(DetailView):
    template_name = 'contact_form_sent.html'
    queryset = ContactMe.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(ContactMe, id=id_)
