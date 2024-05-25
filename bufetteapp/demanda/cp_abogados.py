"""
    Procesador de contextos para traer la lista de abogados
"""
from django.db.models import F, Value, CharField, ExpressionWrapper
from .models import Solicitud, DetalleSolicitud

# def lista_abogados(request):
#     qr = Solicitud.objects.annotate(
#         cliente_id=F('usuario_id'),
#         fecha_solicitud=F('fecha_solicitud'),
#         decision_adoptada=F('decision_adoptada'),
#         abogado_id=F('detallesolicitud__abogado_id')
#         ).values('cliente_id', 'fecha_solicitud', 'decision_adoptada', 'abogado_id')

#     return {'listado': qr}
