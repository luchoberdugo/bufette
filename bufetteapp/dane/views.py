from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Departamento, Ciudad

# Create your views here.
class FiltroCiudades(View):
    """ Esta clase filtrará las ciudades al seleccionar un departamento en la 
        solicitud, usamos ajax para crear la sensación de filtro dinámico
    """

    def get(self, request):
        departamento_id = request.GET.get('depto')

        if departamento_id:
            ciudades  = Ciudad.objects.filter(departamento_id = departamento_id)
            ciudades_filtradas = [{'id': ciudad.id, 'name': ciudad.name} for ciudad in ciudades]

            return JsonResponse(ciudades_filtradas, safe=False)
        else:
            return JsonResponse({'error': 'No se encontraron ciudades'}, safe=False)