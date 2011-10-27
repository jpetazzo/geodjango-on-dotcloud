from django.contrib.gis.db import models

class Place(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=100)
    geom = models.PointField()
    objects = models.GeoManager()
