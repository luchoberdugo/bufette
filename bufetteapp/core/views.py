from django.shortcuts import render, HttpResponseRedirect, redirect
# vistas basadas en clases:
from django.views.generic import ListView, TemplateView, View
# Importamos el modelo de datos de core:
from .models import Contacto, Nosotros, Servicios
# Envio de correos:
from django.core.mail import EmailMessage
#  from django.core.mail import EmailMessage
from django.urls import reverse
# Importamos el forulario:
from .forms import ContactoForm

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

class ContactoPageView(View):
    """ Vista para pagina de Contacto """
    template_name = "core/contacto.html"

    def get(self, request, *args, **kwargs):
        form = ContactoForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwars):
        # Creamos un objeto del formulario y le pasamos los valores
        form = ContactoForm(data = request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']

            mail = EmailMessage(
                    f"Haz recibido un nuevo mensaje de {nombre}",
                    f"De {nombre} <{correo}>\n\nEscribió:\n\n{mensaje}",
                    form.cleaned_data['correo'],
                    ['ederlara@deever.onmicrosoft.com', form.cleaned_data['correo']],
            )

            try:
                mail.fail_silently = False
                mail.send()

                form_contact = form.save(commit=False)
                form_contact.save()
                return redirect(reverse('contacto')+'?ok')
            except:
                # Algo no va bien
                return redirect(reverse('contacto')+'?fail')
        else:
            form.errors
        return render(request, self.template_name, {'form': form})        
        
class ServiciosPageView(ListView):
    """ Vista para pagina de Servicios """
    template_name = "core/servicio.html"
    # Parametros para datos desde la tabla servicios(core_servicios):
    model = Servicios
    paginate_by = 9

        

