from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, ListView, UpdateView, DetailView
from .models import Solicitud, DetalleSolicitud, Expediente, Pruebas, Actuaciones
from .forms import SolicitudForm, DetalleSolicitudForm, ExpedienteForm, PruebasForm, ActuacionesForm

from django.contrib.auth import get_user_model
# Importamos paquete de resolución de urls:
from django.urls import reverse_lazy
# Importamos los elementos necesarios para que funcionen los querys:
from django.db.models import F, Value, CharField, ExpressionWrapper

# Create your views here.
class SolicitudCreateView(CreateView):
    """ Controlador para Crear Solicitud """
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'demanda/solicitud.html'

    def get(self, request, pk):
        usuario = get_user_model().objects.get(id=pk)

        return render(request, self.template_name, {'usuario':usuario, 'form': self.form_class})
    
    def get_success_url(self) -> str:
        return reverse_lazy('solicitud_listar')


class SolicitudesDesatendidasListView(ListView):
    """ Controlador para listar las solicitudes desatendidas """
    model = Solicitud
    paginate_by = 10
    template_name = 'demanda/listasolicituddesatendidas.html'

    def get_queryset(self):
        qs = Solicitud.objects.filter(estado_solicitud = False)
        return qs
    
class SolicitudActivacionView(View):
    """ Controlador para activar una solicitud """
    def get(self, request, pk):
        solicitud = Solicitud.objects.get(id=pk)

        if solicitud.estado_solicitud:
            solicitud.estado_solicitud = True
        else:
            solicitud.estado_solicitud = True
        
        solicitud.save()

        return redirect('asignar_abogado', pk=solicitud.id)




class SolicitudListView(ListView):
    """ Controlador para listar las solicitudes atendidas """
    model = DetalleSolicitud
    paginate_by = 10
    template_name = 'demanda/listasolicitudasignadas.html'

    
class SolicitudView(DetailView):
    model = Solicitud
    # template_name = 'solicitud/solicitud.html'

class SolicitudEditView(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    # template_name =

class DetalleSolicitudCreate(CreateView):
    model = DetalleSolicitud
    form_class = DetalleSolicitudForm
    template_name ='demanda/detallesolicitud.html'

    def get(self, request, pk):
        """ Método para capturar la solicitud """
        try:
            solicitud = Solicitud.objects.get(id=pk)
        except Solicitud.DoesNotExist:
            solicitud = None

        return render(request, self.template_name, {'solicitud': solicitud, 'form': self.form_class})
    
    def get_success_url(self) -> str:
        """ Método para redireccionar a la lista de solicitudes """
        return reverse_lazy('listasolicitudasignadas')
    

class DetalleEditView(UpdateView):
    model = DetalleSolicitud
    form_class = DetalleSolicitudForm
    # template_name

class ExpedienteCreateView(CreateView):
    """ Clase para adicionar expediente a la solicitud """
    model = Expediente
    form_class = ExpedienteForm
    template_name = 'demanda/expediente.html'

    def get(self, request, pk):
        """ Método para capturar la solicitud """
        try:
            solicitud = Solicitud.objects.get(id=pk)
        except Solicitud.DoesNotExist:
            solicitud = None

        return render(request, self.template_name, {'form': self.form_class, 'solicitud': solicitud})
