from rest_framework import serializers


class DeviceSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'name': instance.name,
            'uid': instance.uid
        }

class ReadingSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        context = self.context
        return {
            'id': str(instance.id),
            'created_at': instance.created_at,
            'device_uid': context['device_uid'],
            'parameter': context['parameter'],
            'start_on': context['start_on'],
            'end_on': context['end_on'],
            'reading': instance.reading,
        }