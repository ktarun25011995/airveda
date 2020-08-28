from rest_framework import serializers


class DeviceSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'id': str(instance.id),
            'name': instance.name
        }

class ReadingSerializer(serializers.BaseSerializer):
    def to_representation(self, instance, **kwargs):
        return {
            'id': str(instance.id),
            'created_at': instance.created_at,
            'device_id': kwargs['device_id'],
            'parameter': kwargs['parameter'],
            'start_on': kwargs['start_on'],
            'end_on': kwargs['end_on'],
            'reading': instance.reading,
        }