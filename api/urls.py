from django.urls import re_path
from api import views 


urlpatterns = [
    re_path(r'devices/(?P<device_id>[0-9A-Fa-f-]+)/readings/(?P<parameter>[a-zA-Z_]+)/', views.ReadingView.as_view(), name='reading'),
    re_path(r'devices/(?P<device_id>[0-9A-Fa-f-]+)/', views.DeviceView.as_view(), name='device'),
    re_path(r'devices/', views.DeviceDetailView.as_view(), name='alldevices'),

]