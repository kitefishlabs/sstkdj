from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import mixins, viewsets, permissions, status
from .models import Soundfile, RegionMap, RegionCircle
from .serializers import SoundfileSerializer, RegionMapSerializer, RegionCircleSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView


class SoundfileViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Soundfile.objects.all()
    serializer_class = SoundfileSerializer


class RegionMapViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = RegionMap.objects.all()
    serializer_class = RegionMapSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RegionCircleViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = RegionCircle.objects.all()
    serializer_class = RegionCircleSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'soundfiles': reverse('soundfile-list', request=request, format=format),
        'maps': reverse('map-list', request=request, format=format),
        'regions': reverse('region-list', request=request, format=format)
    })
