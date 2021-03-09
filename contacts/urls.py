from django.urls import path

from contacts.views import ContactCreateView, ContactView

urlpatterns = [
    path('', ContactCreateView.as_view(), name='contact-create'),
    path('<int:id>/', ContactView.as_view(), name='contact-details'),
]
