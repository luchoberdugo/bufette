from django.shortcuts import render
# vistas basadas en clases:
from django.views.generic.base import TemplateView

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