from rest_framework import serializers

from TboProject.models import ObjectLocations


class ObjectLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectLocations
        fields = '__all__'
