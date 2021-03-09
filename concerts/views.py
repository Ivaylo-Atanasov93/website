from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from concerts.models import Concert


class ConcertsListView(ListView):
    template_name = 'concerts.html'
    queryset = Concert.objects.all()