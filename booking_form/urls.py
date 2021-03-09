from django.urls import path
from booking_form.views import BookingCreateView, BookingView

urlpatterns = [
    path('', BookingCreateView.as_view(), name='booking'),
    path('<int:id>/', BookingView.as_view(), name='booking-details'),
]
