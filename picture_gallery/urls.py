from django.urls import path

from picture_gallery.views import PicturesListView, PictureDetailView


urlpatterns = [
    path('', PicturesListView.as_view(), name='photo_gallery'),
    path('details/<int:id>/', PictureDetailView.as_view(), name='image-detail'),
]