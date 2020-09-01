from datetime import datetime

from api.models import Device, TemperatureReading, HumidityReading
from api.serializers import DeviceSerializer, ReadingSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


class DeviceObjectView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            device_uid = str(kwargs['device_uid'])
            device = Device.objects.get(uid=device_uid)
            res = DeviceSerializer(device).data
        except Exception as e:
            return Response({"error": "some error occurred or not found!!"}, status=HTTP_404_NOT_FOUND)

        return Response(res, status=HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        try:
            device_uid = str(kwargs['device_uid'])
            device = Device.objects.get(uid=device_uid)
            device.delete()
        except Exception as e:
            return Response({"error": "some error occurred or not found!! hence won't be able to delete"}, status=HTTP_404_NOT_FOUND)

        return Response({"success": "Successfully deleted!!"}, status=HTTP_200_OK)

class DeviceDetailView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            queryset = Device.objects.all()
            res = DeviceSerializer(queryset, many=True).data
        except Exception as e:
            return Response({"error": "some error occurred or not found!!"}, status=HTTP_404_NOT_FOUND)

        return Response(res, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            device_name = request.data['name']
            uid = request.data['uid']
            device = Device.objects.create(name=device_name, uid=uid)
            res = DeviceSerializer(device).data
        except Exception as e:
            return Response({"error": "some error occurred or device already exits with the name {} ".format(device_name)}, status=HTTP_404_NOT_FOUND)

        return Response(res, status=HTTP_200_OK)


class ReadingView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            device_uid = str(kwargs['device_uid'])
            device = Device.objects.get(uid=device_uid)
            parameter = kwargs['parameter']
            start_on_date = request.GET['start_on']
            end_on_date = request.GET['end_on']
            start_on = datetime.strptime(start_on_date,"%Y-%m-%d %H:%M:%S")
            end_on = datetime.strptime(end_on_date,"%Y-%m-%d %H:%M:%S")

            if parameter == 'humidity':
                res_data = HumidityReading.objects.filter(
                    created_at__gte=start_on,
                    created_at__lte=end_on,
                    device__uid=device_uid
                )
            if parameter == 'temperature':
                res_data = TemperatureReading.objects.filter(
                    created_at__gte=start_on,
                    created_at__lte=end_on,
                    device__uid=device_uid
                )
            
            res  = ReadingSerializer(res_data, many=True, context={
                    'device_uid':device_uid,
                    'start_on':start_on_date,
                    'end_on': end_on_date,
                    'parameter': parameter
                }).data
        except Exception as e:
            return Response({"error": "some error occurred or not found!!"}, status=HTTP_404_NOT_FOUND)

        return Response(res, status=HTTP_200_OK)