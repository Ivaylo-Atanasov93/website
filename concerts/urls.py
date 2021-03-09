from django.urls import path

from concerts.views import ConcertsListView

urlpatterns = [
    path('', ConcertsListView.as_view(), name='concerts'),
]