from django.contrib import admin
from .models import Diagnose, Service, DoctorsSchedule, Order, DayofWeek, WorkingTime

admin.site.register(Diagnose)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'img', 'doctor')
admin.site.register(Service, ServicesAdmin)

admin.site.register(Order)
admin.site.register(DayofWeek)
admin.site.register(WorkingTime)

class DoctorsScheduleAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day_of_week', 'working_time')
admin.site.register(DoctorsSchedule, DoctorsScheduleAdmin)