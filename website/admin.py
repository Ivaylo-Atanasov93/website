from django.contrib import admin

from biography.models import Biography
from booking_form.models import Booking
from concerts.models import Concert
from contacts.models import ContactMe
from index.models import Quotes
from video_gallery.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_url', 'date')
    list_filter = ('title', 'date')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time')
    list_filter = ('name', 'date', 'time')


class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'message')
    list_filter = ('name', 'date')


class ConcertAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'time', 'location')
    list_filter = ('location', 'date')


class BiographyAdmin(admin.ModelAdmin):
    list_display = (
        'summary_title',
        'summary',
        'academic_achievements_title',
        'academic_achievements',
        'childhood_title',
        'childhood_1',
        'childhood_2',
        'childhood_3',
        'final_thoughts_title',
        'final_thoughts',
    )



class QuotesAdmin(admin.ModelAdmin):
    list_display = ('author', 'quotes')
    list_filter = ('author', 'quotes')


admin.site.register(Quotes, QuotesAdmin)
admin.site.register(Biography, BiographyAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(ContactMe, ContactMeAdmin)
admin.site.register(Concert, ConcertAdmin)
