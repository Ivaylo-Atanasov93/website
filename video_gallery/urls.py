from django.urls import path

from video_gallery.views import VideoListView

urlpatterns = [
    path('', VideoListView.as_view(), name='video_gallery')
]