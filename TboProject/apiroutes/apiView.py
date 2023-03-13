from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from ..databases.serialazers import ObjectSerializer
from ..models import ObjectLocations


class ObjectAPIView(APIView):
    def get(self, request):
        lst = ObjectLocations.objects.all().values()
        return Response({'db': list(lst)})


#
# class ObjectAPIView(generics.ListAPIView):
#     queryset = ObjectLocations.objects.all()
#     serializer_class = ObjectSerializer