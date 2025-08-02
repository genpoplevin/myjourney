from django.contrib import admin
from .models import Journey, Place


class PlaceInline(admin.TabularInline):
    model = Place
    extra = 1


class JourneyAdmin(admin.ModelAdmin):
    list_display = ('location', 'cost')
    inlines = [PlaceInline]


admin.site.register(Journey, JourneyAdmin)
admin.site.register(Place)
