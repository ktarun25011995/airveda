from django.urls import re_path
from api import views 


urlpatterns = [
    re_path(r'devices/(?P<device_uid>\w+)/readings/(?P<parameter>[a-zA-Z_]+)/', views.ReadingView.as_view(), name='reading'),
    re_path(r'devices/(?P<device_uid>\w+)/', views.DeviceObjectView.as_view(), name='device'),
    re_path(r'devices/', views.DeviceDetailView.as_view(), name='alldevices'),

]