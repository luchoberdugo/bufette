from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
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
        #usuario = self.form_class(initial={'usuario': user})

        return render(request, self.template_name, {'usuario':usuario, 'form': self.form_class})
    
    def get_success_url(self) -> str:
        return reverse_lazy('listasolicitud')

class SolicitudListView(ListView):
    model = Solicitud
    paginate_by = 10
    template_name = 'demanda/listasolicitud.html'

    # def get_queryset(self):
    #     qr = Solicitud.objects.annotate(
    #     cliente_id=F('usuario_id'),
    #     fecha_solicitud=F('fecha_solicitud'),
    #     decision_adoptada=F('decision_adoptada'),
    #     abogado_id=F('detallesolicitud__abogado_id')
    #     ).values('cliente_id', 'fecha_solicitud', 'decision_adoptada', 'abogado_id')
    #     return qr
    
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
    # template_name =

class DetalleEditView(UpdateView):
    model = DetalleSolicitud
    form_class = DetalleSolicitudForm
    # template_name

class ExpedienteCreateView(CreateView):
    model = Expediente
    form_class = ExpedienteForm
    # template_name =