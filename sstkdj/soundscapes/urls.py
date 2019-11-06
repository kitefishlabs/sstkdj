from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SoundfileViewSet, RegionMapViewSet, RegionCircleViewSet, api_root
from rest_framework import renderers


router = DefaultRouter()
router.register(r'soundfiles', SoundfileViewSet)
router.register(r'maps', RegionMapViewSet)
router.register(r'regions', RegionCircleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
