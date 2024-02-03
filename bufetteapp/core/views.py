from django.shortcuts import render
# vistas basadas en clases:
from django.views.generic.base import TemplateView

# Create your views here.
class IndexPageView(TemplateView):
    # indicar template que se usa en esta vista
    template_name = "core/index.html"
    

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class NosotrosPageView(TemplateView):
    template_name = "core/nosotros.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)    