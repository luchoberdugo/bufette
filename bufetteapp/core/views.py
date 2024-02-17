from django.shortcuts import render
# vistas basadas en clases:
from django.views.generic import ListView, TemplateView
# Importamos el modelo de datos de core:
from .models import Contacto, Nosotros, Servicios

# Create your views here.
class IndexPageView(TemplateView):
    """ Vista para el index de la aplicación """
    template_name = "core/index.html"
    
    def get(self, request, *args, **kwargs):
        """ Este método se encarga de enviar al request de la pág. 
            para que se muestre la info en el template """
        return render(request, self.template_name)

class NosotrosPageView(TemplateView):
    """ Vista para la página de nosotros """
    template_name = "core/nosotros.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)    

class ContactoPageView(TemplateView):
    """ Vista para pagina de Contacto """
    template_name = "core/contacto.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
        
class ServiciosPageView(ListView):
    """ Vista para pagina de Servicios """
    template_name = "core/servicio.html"
    # Parametros para datos desde la tabla servicios(core_servicios):
    model = Servicios
    paginate_by = 9

        

