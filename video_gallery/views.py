from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from video_gallery.models import Video


class VideoListView(ListView):
    template_name = '../templates/videos.html'
    model = Video
    queryset = Video.objects.all()
