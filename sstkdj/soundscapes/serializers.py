from rest_framework import serializers
from .models import Soundfile, RegionMap, RegionCircle, EmailUser
import wave
from hashlib import md5
from os.path import basename


class SoundfileSerializer(serializers.HyperlinkedModelSerializer):

    def calculate_checksum(self, name, chans, rate, samp_length):
        asstr = str(basename(name)) + str(samp_length) + \
            str((int(rate / 100) << 20) + (chans << 4))
        return md5(bytes(asstr, encoding='utf8')).hexdigest()

    def create(self, validated_data):
        sfile = validated_data['file']
        wav = wave.open(sfile, mode='rb')
        try:
            chnls = int(wav.getnchannels())
            rate = int(wav.getframerate())
            dur = int(wav.getnframes())
        except:
            chnls = 0
            rate = 0
            dur = 0
        validated_data['channels'] = chnls
        validated_data['sample_rate'] = rate
        validated_data['length'] = dur
        wav.close()
        checksum = self.calculate_checksum(
            sfile.name, chnls, rate, dur)
        validated_data['checksum'] = checksum
        return Soundfile.objects.create(**validated_data)

    class Meta:
        model = Soundfile
        owner = serializers.StringRelatedField(source='owner.email')
        fields = ['id', 'url', 'owner', 'name', 'file',
                  'length', 'sample_rate', 'channels', 'checksum', ]


class RegionMapSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = RegionMap
        fields = ['id', 'url', 'owner', 'name', 'regions', ]


class RegionCircleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = RegionCircle
        fields = ['id', 'url', 'owner', 'label', 'center_latitude', 'center_longitude',
                  'radius', 'active', 'attack', 'release', 'lives', 'soundfile', 'loops', 'finish_rule', 'state', 'assigned_slot', 'pause_offset', 'region_map']
