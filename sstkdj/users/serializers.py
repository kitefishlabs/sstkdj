from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import EmailUser
from sstkdj.soundscapes.models import Soundfile, RegionMap, RegionCircle


class EmailUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EmailUser
        fields = ['url', 'username', 'email', 'groups',
                  'maps', 'soundfiles', 'regions']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
