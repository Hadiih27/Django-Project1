
from django.contrib import admin
from .models import TransportSchedule

class TransportScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'direction')  

admin.site.register(TransportSchedule, TransportScheduleAdmin)
