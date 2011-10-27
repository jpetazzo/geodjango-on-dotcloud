from django.contrib.gis import admin
from models import Place

admin.site.register(Place, admin.OSMGeoAdmin)

