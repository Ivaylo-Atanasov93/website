from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Picture


# Create your views here.

class PicturesListView(ListView):
    template_name = 'photo_gallery.html'
    model = Picture
    queryset = Picture.objects.all()


class PictureDetailView(DetailView):
    template_name = 'img_detail.html'
    queryset = Picture.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Picture, id=id_)

# class PictureDetailView(DetailView):
#     template_name = '../templates/img_detail.html'
#     queryset = Picture.objects.all()
