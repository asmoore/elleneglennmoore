from django.contrib import admin
from models import Biography, Event, Work

admin.site.register(Biography)

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_date', 'event_title', 'event_description')
admin.site.register(Event, EventAdmin)

class WorkAdmin(admin.ModelAdmin):
    list_display = ('work_type', 'work_text')
admin.site.register(Work, WorkAdmin)
