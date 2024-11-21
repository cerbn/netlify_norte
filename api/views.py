# api/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OrdenDespacho
from .serializers import OrdenDespachoSerializer

@api_view(['POST'])
def agregar_venta(request):
    # Procesa la solicitud POST para agregar una nueva OrdenDespacho
    serializer = OrdenDespachoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(1, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def estado_seguimiento(request):
    id_orden = request.data.get('id_orden')
    try:
        orden = OrdenDespacho.objects.using('supabase').get(id_orden=id_orden)
        return Response({'estado_envio': orden.estado_envio}, status=status.HTTP_200_OK)
    except OrdenDespacho.DoesNotExist:
        return Response(
            {"detail": "No se encontró un estado para el número de orden especificado."},
            status=status.HTTP_404_NOT_FOUND
        )
