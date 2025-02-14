from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Partitura
from .serializers import PartituraSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def menu(request):
    partituras = Partitura.objects.filter(usuario=request.user)
    serializer = PartituraSerializer(partituras, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def catalogo(request):
    partituras = Partitura.objects.filter(usuario=request.user)
    serializer = PartituraSerializer(partituras, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subir_partitura(request):
    serializer = PartituraSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def actualizar_partitura(request, partitura_id):
    partitura = get_object_or_404(Partitura, pk=partitura_id, usuario=request.user)
    serializer = PartituraSerializer(partitura, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_partitura(request, partitura_id):
    partitura = get_object_or_404(Partitura, pk=partitura_id, usuario=request.user)
    partitura.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def visualizar_partitura(request, partitura_id):
    partitura = get_object_or_404(Partitura, pk=partitura_id, usuario=request.user)
    serializer = PartituraSerializer(partitura)
    return Response(serializer.data)