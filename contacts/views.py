from django.core.mail import send_mail
import logging
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.
from django.views.generic import CreateView, DetailView

from contacts.forms import ContactMeForm
from contacts.models import ContactMe


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactMeForm
    model = ContactMe
    queryset = ContactMe.objects.all()

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        customers_message = form.cleaned_data.get('message')
        message = f'Message from {name}\n\n'
        message += f'\n\n{customers_message}\n\n'
        message += f'Contacts:\n\nE-mail: {email}'
        send_mail(
            subject=f'New booked lesson from {name}!',
            message=message,
            from_email='dimitar.kanchev.website@gmail.com',
            recipient_list=[email, 'dimitar.kanchev1993@gmail.com'],
        )

        return super().form_valid(form)


# def basic_view(request):
#     print(request.POST)
#     # print(f'I AM IN THE FORM, THIS IS THE INFO: {form.cleaned_data}')
#     # name = form.cleaned_data.get('name')
#     # print(f'HERE IS THE NAME: {name}')
#     # email = form.cleaned_data.get('email')
#     # customers_message = form.cleaned_data.get('message')
#     # response = {'topic': "Hello WOrld"}
#     return JsonResponse(['wagwan'])


class ContactView(DetailView):
    template_name = 'contact_form_sent.html'
    queryset = ContactMe.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(ContactMe, id=id_)
