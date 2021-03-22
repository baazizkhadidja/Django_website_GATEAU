
from .models import Gateau
from .serializers import GatSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets


#fonction classique

@api_view(['GET'])
def gateau_API(request):
    all_gat = Gateau.objects.all()
    data = GatSerializer(all_gat, many=True).data
    return Response(data)

@api_view(['GET'])
def gateau_detail_api(request, id):
    gateau_detail = Gateau.objects.get(id = id)
    data = GatSerializer(gateau_detail).data
    return Response({'data': data})


# classe générique:

#API qui permet  GET + POST + DELETE
class GateauDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gateau.objects.all()
    serializer_class = GatSerializer
    lookup_field = 'id'
    


#API qui permet GET
class GateauListApi(generics.ListAPIView):
    queryset = Gateau.objects.all()
    serializer_class = GatSerializer
    

#API qui permet GET +  add 
class GateauAdd(generics.ListCreateAPIView):
    queryset = Gateau.objects.all()
    serializer_class = GatSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Gateau.objects.all()
    serializer_class = GatSerializer
