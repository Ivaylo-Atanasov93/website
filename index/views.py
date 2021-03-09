from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from index.models import Quotes


class IndexView(ListView):
    template_name = 'index.html'
    model = Quotes
    queryset = Quotes.objects.all()
