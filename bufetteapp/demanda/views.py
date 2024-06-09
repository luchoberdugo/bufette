from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View, CreateView, ListView, UpdateView, DetailView
from .models import Solicitud, DetalleSolicitud, Expediente, Pruebas, Actuaciones
from .forms import SolicitudForm, DetalleSolicitudForm, ExpedienteForm, PruebasForm, ActuacionesForm

from django.contrib.auth import get_user_model
# Importamos paquete de resolución de urls:
from django.urls import reverse, reverse_lazy
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
    success_url = reverse_lazy('listasolicitudasignadas')

    def get(self, request, pk):
        """ Método para capturar la solicitud """
        try:
            solicitud = Solicitud.objects.get(id=pk)
        except Solicitud.DoesNotExist:
            solicitud = None

        return render(request, self.template_name, {'solicitud': solicitud, 'form': self.form_class})
    

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
            deta_solicitud = DetalleSolicitud.objects.filter(solicitud = solicitud)
        except Solicitud.DoesNotExist:
            solicitud = None
            deta_solicitud = None

        return render(request, self.template_name, {'exp_form': self.form_class,
                                                    'solicitud': solicitud, 
                                                    'deta_solicitud': deta_solicitud})
    def get_success_url(self):
        """ Método para redireccionar al guardar """
        return reverse_lazy('expediente_listar', kwargs={'pk': self.kwargs['pk']})

class ExpedienteListView(ListView):
    """ Clase para listar expedientes de la solicitud """
    model = Expediente
    paginate_by = 10
    template_name = 'demanda/listaexpedientes.html'


class PruebasExpedienteView(TemplateView):
    """ Clase para adicionar pruebas y actos a la """
    template_name = 'demanda/pruebas.html'
    form_class =  PruebasForm

    def get(self, request, pk):
        """ Método para capturar el expediente """
        try:
            expediente = Expediente.objects.get(id=pk)
            solicitud = Solicitud.objects.filter(id= expediente.solicitud_id)
            for sol in solicitud:
                deta_solicitud = DetalleSolicitud.objects.filter(solicitud = sol.id)
        except Expediente.DoesNotExist:
            expediente = None
            solicitud = None

        return render(request,self.template_name, {'prueba_form': self.form_class,
                                                   'solicitud': solicitud,
                                                   'expediente': expediente,
                                                   'deta_solicitud': deta_solicitud})
    
    def post(self, request, *args, **kwargs):
        """ Método para guardar los datos del formulario """
        prueba_form = PruebasForm(data = request.POST)
        actos_form = ActuacionesForm(data = request.POST)

        if 'guarda_prueba' in request.POST:
            if prueba_form.is_valid():
                prueba = prueba_form.save(commit=False)
                prueba.save()
            else:
                prueba_form.errors
        
        elif 'guarda_acto' in request.POST:
            if actos_form.is_valid():
                acto = actos_form.save(commit=False)
                acto.save()
            else:
                actos_form.errors

        return HttpResponseRedirect(reverse('informeexpediente', kwargs={'pk': self.kwargs['pk']}))
                    

class ExpedienteInformeView(TemplateView):
    """ Clase para adicionar pruebas y actos a la """
    template_name = 'demanda/expedienteinforme.html'

    def get(self, request, pk):
        """ Método para capturar el expediente """
        try:
            expediente = Expediente.objects.get(id=pk)
            solicitud = Solicitud.objects.filter(id= expediente.solicitud_id)
            for sol in solicitud:
                deta_solicitud = DetalleSolicitud.objects.filter(solicitud = sol.id)
            pruebas = Pruebas.objects.filter(expediente = expediente)
            actos = Actuaciones.objects.filter(expediente = expediente)

        except Expediente.DoesNotExist:
            expediente = None
            solicitud = None

        return render(request,self.template_name, {'prueba_exp': pruebas,
                                                   'actos_exp': actos,
                                                   'solicitud': solicitud,
                                                   'expediente': expediente,
                                                   'deta_solicitud': deta_solicitud})
    

class ActuacionesExpedienteView(TemplateView):
    """ Clase para adicionar pruebas y actos a la """
    model = Actuaciones
    template_name = 'demanda/actuaciones.html'
    form_class =  ActuacionesForm

    def get(self, request, pk):
        """ Método para capturar el expediente """
        try:
            expediente = Expediente.objects.get(id=pk)
            solicitud = Solicitud.objects.filter(id= expediente.solicitud_id)
            for sol in solicitud:
                deta_solicitud = DetalleSolicitud.objects.filter(solicitud = sol.id)
        except Expediente.DoesNotExist:
            expediente = None
            solicitud = None

        return render(request,self.template_name, {'actos_form': self.form_class,
                                                   'solicitud': solicitud,
                                                   'expediente': expediente,
                                                   'deta_solicitud': deta_solicitud})
    
    def post(self, request, *args, **kwargs):
        """ Método para guardar los datos del formulario """
        actos_form = ActuacionesForm(data = request.POST)
        
        if 'guarda_acto' in request.POST:
            if actos_form.is_valid():
                acto = actos_form.save(commit=False)
                acto.save()
            else:
                actos_form.errors

        return HttpResponseRedirect(reverse('informeexpediente', kwargs={'pk': self.kwargs['pk']}))



