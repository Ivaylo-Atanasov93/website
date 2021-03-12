from django.contrib import admin

from biography.models import Biography, Education, PersonalExperience, Achievements, WorkExperience, Languages, \
    Passions
from booking_form.models import Booking
from concerts.models import Concert
from contacts.models import ContactMe
from index.models import Quotes
from picture_gallery.models import Picture
from video_gallery.models import Video


class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo_url', 'date')
    list_filter = ('title', 'date')


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_url', 'date')
    list_filter = ('title', 'date')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'date', 'time')
    list_filter = ('name', 'date', 'time')


class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'date', 'message')
    list_filter = ('name', 'surname', 'date')


class ConcertAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'time', 'location')
    list_filter = ('location', 'date')


class EducationInLine(admin.StackedInline):
    model = Education
    extra = 0


class PersonalExperienceInLine(admin.StackedInline):
    model = PersonalExperience
    extra = 0


class AchievementsInLine(admin.StackedInline):
    model = Achievements
    extra = 0


class WorkExperienceInLine(admin.StackedInline):
    model = WorkExperience
    extra = 0


class LanguagesInLine(admin.StackedInline):
    model = Languages
    extra = 0


class PassionsInLine(admin.StackedInline):
    model = Passions
    extra = 0


class BiographyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        EducationInLine,
        PersonalExperienceInLine,
        WorkExperienceInLine,
        AchievementsInLine,
        LanguagesInLine,
        PassionsInLine,
    ]


class QuotesAdmin(admin.ModelAdmin):
    list_display = ('author', 'quotes')
    list_filter = ('author', 'quotes')


admin.site.register(Quotes, QuotesAdmin)
admin.site.register(Biography, BiographyAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(ContactMe, ContactMeAdmin)
admin.site.register(Concert, ConcertAdmin)
