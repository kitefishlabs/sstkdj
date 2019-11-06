from django.db import models
from sstkdj.users.models import EmailUser


class Soundfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        EmailUser, related_name='soundfiles', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, default='NO-NAME')
    file = models.FileField(blank=False, null=True)
    length = models.IntegerField(default=48000)
    sample_rate = models.IntegerField(default=48000)

    def __str__(self):
        return (self.name + ' - ' + str(self.length / self.sample_rate) + ' - ' + str(self.updated))


class RegionMap(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        EmailUser, related_name='maps', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return (self.name + ' - ' + str(self.updated))


class RegionCircle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        EmailUser, related_name='owned_regions', on_delete=models.SET_NULL, null=True)
    region_map = models.ForeignKey(
        RegionMap, related_name='regions', on_delete=models.SET_NULL, null=True)
    soundfile = models.CharField(
        max_length=200, blank=True, default='')
    label = models.CharField(max_length=100, blank=True, default='')
    center_latitude = models.FloatField(
        'latitude', default=0.0)
    center_longitude = models.FloatField(
        'longitude', default=0.0)
    radius = models.FloatField(default=0.01)
    active = models.BooleanField(default=True)
    attack = models.IntegerField(default=1000)
    release = models.IntegerField(default=1000)
    lives = models.IntegerField(default=99)

    loops = models.IntegerField(null=True)
    finish_rule = models.BooleanField(default=False)
    state = models.CharField(max_length=10, null=True)
    assigned_slot = models.IntegerField(null=True)
    pause_offset = models.FloatField(default=0.0)

    def __str__(self):
        return (self.label + ' - (' + str(self.center_latitude) + ', ' + str(self.center_longitude) + ', ' + str(self.radius) + ') - ' + str(self.updated))
