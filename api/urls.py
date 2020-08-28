from django.urls import re_path
from .views import DeviceView, DeviceDetailView, ReadingView


urlpatterns = [
    re_path(r'devices/(?P<device_id>[0-9A-Fa-f-]+)/readings/<str:parameter>/', ReadingView.as_view(), name='reading'),
    re_path(r'devices/(?P<device_id>[0-9A-Fa-f-]+)/', DeviceView.as_view(), name='device'),
    re_path(r'devices/', DeviceDetailView.as_view(), name='alldevices'),

]