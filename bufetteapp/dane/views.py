from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Departamento, Ciudad

# Create your views here.
class FiltroCiudades(View):

    def get(self, request):
        # filtrado = {}
        departamento_id = request.GET.get('departamento')
        filtrado = []

        if departamento_id:
            ciudades = Ciudad.objects.filter(departamento_id = departamento_id)

            for city in ciudades:
                print(city.name)
                filtrado_d = {
                    'id': city.id,
                    'nombre': city.name
                }
            if filtrado_d not in filtrado:
                filtrado.append(filtrado_d)
            filtrado = dict(filtrado)
            print(filtrado)
            return JsonResponse(filtrado)
        else:
            return JsonResponse({'error': 'No se encontraron ciudades'})