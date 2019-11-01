from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import EmailUser
from sstkdj.soundscapes.models import RegionMap


class EmailUserSerializer(serializers.HyperlinkedModelSerializer):
    maps = serializers.PrimaryKeyRelatedField(
        many=True, queryset=RegionMap.objects.all())

    class Meta:
        model = EmailUser
        fields = ['url', 'username', 'email', 'groups', 'maps', ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
