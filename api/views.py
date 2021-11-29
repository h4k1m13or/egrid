from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import django_filters
# Create your views here.
from api.serializers import PLNTSerializer, STSerializer
from main.models import PLNT, State
from api.apps import ApiConfig


class PlantsList(generics.ListAPIView):
    serializer_class = PLNTSerializer
    queryset = PLNT.objects.all().order_by('-PLNGENAN')
    filterset_fields = ['PSTATABB', 'PLNGENAN']
    search_fields = ['PNAME']


class PlantDetail(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        plant = PLNT.objects.filter(id=id).first()
        if not plant:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        data = ApiConfig.dataplant
        rs = data.loc[data['SEQPLT19'] == plant.SEQPLT19].to_dict('records')
        print(rs[0])
        return Response(rs[0], status=status.HTTP_200_OK)


class StatesList(generics.ListAPIView):
    serializer_class = STSerializer
    queryset = State.objects.all().order_by('-STNGENAN')
    filterset_fields = ['PSTATABB']
    search_fields = ['PSTATABB']


class StateDetail(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        state = State.objects.filter(id=id).first()
        if not state:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        data = ApiConfig.datastate
        rs = data.loc[data['PSTATABB'] == state.PSTATABB].to_dict('records')
        print(rs[0])
        return Response(rs[0], status=status.HTTP_200_OK)
