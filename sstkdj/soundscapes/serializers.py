from rest_framework import serializers
from .models import Soundfile, RegionMap, RegionCircle


class SoundfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Soundfile
        fields = ['id', 'owner', 'name', 'filepath', 'length',
                  'sample_rate', 'regions_assigned_to', ]


class RegionMapSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = RegionMap
        fields = ['id', 'owner', 'name', 'regions', ]


class RegionCircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionCircle
        fields = ['id', 'label', 'center_latitude', 'center_longitude',
                  'radius', 'active', 'attack', 'release', 'lives', 'soundfile', 'loops', 'finish_rule', 'state', 'assigned_slot', 'pause_offset']
