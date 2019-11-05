from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import EmailUser
from sstkdj.soundscapes.models import Soundfile, RegionMap, RegionCircle


class EmailUserSerializer(serializers.HyperlinkedModelSerializer):
    soundfiles = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Soundfile.objects.all())
    maps = serializers.PrimaryKeyRelatedField(
        many=True, queryset=RegionMap.objects.all())
    regions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=RegionCircle.objects.all())

    class Meta:
        model = EmailUser
        fields = ['url', 'username', 'email', 'groups', 'maps', ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
