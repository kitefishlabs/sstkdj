from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SoundfileViewSet, RegionMapViewSet, RegionCircleViewSet, api_root
from rest_framework import renderers

soundfile_list = SoundfileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
soundfile_detail = SoundfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

regionmap_list = RegionMapViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
regionmap_detail = RegionMapViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

regioncircle_list = RegionCircleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
regioncircle_detail = RegionCircleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', api_root),
    path(r'soundfiles/', soundfile_list, name='soundfile-list'),
    path(r'soundfiles/<int:pk>', soundfile_detail,
         name='soundfile-detail'),
    path(r'maps/', regionmap_list, name='map-list'),
    path(r'maps/<int:pk>', regionmap_detail, name='map-detail'),
    path(r'regions/', regioncircle_list, name='region-list'),
    path(r'regions/<int:pk>', regioncircle_detail,
         name='regioncircle-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
