from rest_framework import viewsets, permissions
from .models import Soundfile, RegionMap, RegionCircle
from .serializers import SoundfileSerializer, RegionMapSerializer, RegionCircleSerializer
from .permissions import IsOwnerOrReadOnly


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
