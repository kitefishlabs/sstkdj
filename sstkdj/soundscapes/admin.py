from django.contrib import admin
from .models import Soundfile, RegionMap, RegionCircle

admin.site.register(Soundfile)
admin.site.register(RegionMap)
admin.site.register(RegionCircle)
