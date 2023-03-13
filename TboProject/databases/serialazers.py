from rest_framework import serializers

from TboProject.models import ObjectLocations


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectLocations
        fields = ('id', 'name')