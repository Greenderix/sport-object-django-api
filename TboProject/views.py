from rest_framework import filters, mixins
from rest_framework.viewsets import GenericViewSet

from TboProject.models import ObjectLocations
from TboProject.serializers import ObjectLocationSerializer


class ObjectAPIView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = ObjectLocations.objects.all()
    serializer_class = ObjectLocationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$addres', '$activ']
