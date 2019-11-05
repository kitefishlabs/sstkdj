from rest_framework import serializers
from .models import Soundfile, RegionMap, RegionCircle


class SoundfileSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Soundfile
        fields = ['id', 'url', 'owner', 'name', 'filepath', 'length',
                  'sample_rate', ]


class RegionMapSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = RegionMap
        fields = ['id', 'url', 'owner', 'name', 'regions', ]


class RegionCircleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = RegionCircle
        fields = ['id', 'url', 'label', 'center_latitude', 'center_longitude',
                  'radius', 'active', 'attack', 'release', 'lives', 'soundfile', 'loops', 'finish_rule', 'state', 'assigned_slot', 'pause_offset', 'owner', ]
