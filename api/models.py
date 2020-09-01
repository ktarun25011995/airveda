import uuid
from django.utils import timezone
from django.db import models
from datetime import datetime


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=datetime.now)
    uid = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=False, unique=True)
    
    def __str__(self):
        return "Device - {}".format(self.name)


class TemperatureReading(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=datetime.now)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING, null=True)
    reading = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return "Reading {}".format(str(self.id))


class HumidityReading(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=datetime.now)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING, null=True)
    reading = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return "Reading {}".format(str(self.id))