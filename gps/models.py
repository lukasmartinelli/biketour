from django.db import models


class Point(models.Model):
    time = models.DateTimeField(db_index=True)
    lat = models.FloatField()
    lon = models.FloatField()
    accuracy = models.FloatField(null=True)
    speed = models.FloatField(null=True)
    battery = models.FloatField(null=True)
    satellites = models.FloatField(null=True)
    direction = models.FloatField(null=True)
    provider = models.CharField(max_length=50, null=True)
    native_altitude = models.FloatField(null=True)
    google_altitude = models.FloatField(null=True)
