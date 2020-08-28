from rest_framework import serializers


class DeviceSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'id': str(instance.id),
            'name': instance.name
        }

class ReadingSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        context = self.context
        return {
            'id': str(instance.id),
            'created_at': instance.created_at,
            'device_id': context['device_id'],
            'parameter': context['parameter'],
            'start_on': context['start_on'],
            'end_on': context['end_on'],
            'reading': instance.reading,
        }