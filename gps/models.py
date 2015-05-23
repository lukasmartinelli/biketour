from django.db import models


class Point(models.Model):
    time = models.DateTimeField()
    lat = models.FloatField()
    lon = models.FloatField()
    accuracy = models.FloatField()
    speed = models.FloatField()
    battery = models.FloatField()
    satellites = models.FloatField()
    direction = models.FloatField()
    provider = models.CharField(max_length=50)
    native_altitude = models.FloatField()
    google_altitude = models.FloatField()
