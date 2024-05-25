from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, View, CreateView, ListView, UpdateView, DetailView
from .models import Solicitud, DetalleSolicitud, Expediente, Pruebas, Actuaciones
from .forms import SolicitudForm, DetalleSolicitudForm, ExpedienteForm, PruebasForm, ActuacionesForm

# Create your views here.
class SolicitudCreateView(CreateView):
    """ Controlador para Crear Solicitud """
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'demanda/solicitud.html'

class SolicitudListView(ListView):
    model = Solicitud
    paginate_by = 10
    # template_name =

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()
    
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