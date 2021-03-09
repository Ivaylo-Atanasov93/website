# Create your views here.
from django.views.generic import ListView

from biography.models import Biography


class BiographyListView(ListView):
    template_name = 'biography.html'
    model = Biography
    queryset = Biography.objects.all()
