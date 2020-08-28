from django.contrib import admin
from api.models import Device, TemperatureReading, HumidityReading

admin.site.register(Device)
admin.site.register(TemperatureReading)
admin.site.register(HumidityReading)
