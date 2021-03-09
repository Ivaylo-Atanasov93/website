from django.urls import path

from biography.views import BiographyListView

urlpatterns = [
    path('', BiographyListView.as_view(), name='biography')
]