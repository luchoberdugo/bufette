from django.db.models.base import Model as Model
from django.contrib.auth.models import Group
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View, DetailView
# Importamos el formulario:
from .forms import SignUpUserFormWithEmail, DetalleUserForm, UserUtilForm, IdProfessionalForm, TelefonoUserForm
# importamos el modelo de datos:
from .models import Usuario, DetalleUsuario, TarjetaProfesional, TelefonoUser
from django.db.models import Q

# Método decorador de login:
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

# Importamos paquete de resolución de urls:
from django.urls import reverse_lazy

# ---------------------------------  CRUD DE USUARIO COMPLETO ---------------------------------

# Create your views here.
# ---------------------------------  CRUD DE USUARIO Registro ---------------------------------
  
class SignUpUserView(LoginRequiredMixin, CreateView):
    form_class = SignUpUserFormWithEmail
    template_name = 'registration/registro.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        # Agrega el correo electrónico a la URL de redirección
        email = self.request.POST["email"]
        return reverse_lazy('detalle_usuario') + f'?email={email}'      # Se cambia el parámetro de url para poder buscar el id mas adelante en la pantala siguiente
    
class AddDetailUserView(CreateView):
    """ Clase para agregar datos en el detalle del usuario """
    template_name = 'registration/detalleuser.html'
    form_class = DetalleUserForm
    
    def get(self, request, *args, **kwargs):
        """ Con este método get vamos a capturar el id del usuario, 
            tambien podemos tener todo el usuario para pintarlo en la pantalla """
        # Capturamos el email del usuario guardado:
        email = request.GET.get('email')
        # Consultamos en la bd y capturamos el id:
        try:
            usuario = Usuario.objects.get(email=email)      # Buscamos el usuario que tenga el email que pasamos en la url
        except Usuario.DoesNotExist:
            usuario = None
        
        return render(request, self.template_name, {'usuario': usuario, 'form': self.form_class})

    def get_success_url(self) -> str:
        """ Redirige al dashboard una vez que se completa el formulario """
        return reverse_lazy('listausuario')
    
    
@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    """ Clase para ver el listado de usuarios """
    model = Usuario
    template_name = 'registration/userlist.html'
    paginate_by = 10

    # Método para filtrar:
    def get_queryset(self):
        qs = super().get_queryset()         # De entrada capturamos todos los datos
        filtro = self.request.GET.get('query')

        if filtro :
            qs = qs.filter(
                Q(first_name__icontains=filtro) | Q(last_name__icontains=filtro)
            )
        return qs.order_by('groups__name','-is_active')

class UserEditView(UpdateView):
    template_name = 'registration/useredit.html'
    form_class = UserUtilForm

    def get_object(self):
        user_obj, created = Usuario.objects.get_or_create(id=self.kwargs['pk'])
        if user_obj.is_active:
            user_obj.is_active = True
        return user_obj 

    def get_success_url(self) -> str:
        """ Redirige al dashboard una vez que se completa el formulario """  
        return reverse_lazy('listausuario')

class UserActivateOrDeactivateView(View):
    
    def get(self, request, pk):
        user = get_user_model().objects.get(id=pk)

        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True
        
        user.save()

        return redirect('listausuario')
    
# ---------------------------------  CRUD DE USUARIO Telefono ---------------------------------

class TelefonoUserAdd(CreateView):
    form_class = TelefonoUserForm
    template_name = 'registration/telefonouser.html'
    telefonos = []

    def get(self, request, pk):
        """ Con este método get vamos a capturar el id del usuario abogado,"""
        usuario = get_user_model().objects.get(id=pk)
        telefono_user = TelefonoUser.objects.filter(usuario = usuario)

        for phone in telefono_user:
            phone_detail = {
                'id': phone.id,
                'tipo_telefono': phone.tipo_telefono,
                'numero': phone.numero_tel,
                'usuario': phone.usuario
            }
            if phone_detail not in self.telefonos:
                self.telefonos.append(phone_detail)

        return render(request, self.template_name, { 'usuario': usuario, 'form': self.form_class, 'telefonos': self.telefonos})

    def get_success_url(self) -> str:
        """ Redirige al dashboard una vez que se completa el formulario """
        return reverse_lazy('listausuario')

# ---------------------------------  CRUD DE USUARIO Tarjeta Profesional ---------------------------------   

class AddIdProfessionalView(CreateView):
    """ Clase para agregar la tarjeta profesional del usuario abogado """
    template_name = 'registration/tarjeta_form.html'
    form_class = IdProfessionalForm

    def get(self, request, pk):
        """ Con este método get vamos a capturar el id del usuario abogado,"""
        abogado = get_user_model().objects.get(id=pk)
        return render(request, self.template_name, { 'abogado': abogado, 'form': self.form_class})
    
    def get_success_url(self) -> str:
        """ Redirige al dashboard una vez que se completa el formulario """
        return reverse_lazy('listausuario')
    
class UpdateIdProfessionalView(UpdateView):
    """ Clase para agregar la tarjeta profesional del usuario abogado """
    template_name = 'registration/tarjeta_form.html'
    form_class = IdProfessionalForm

    def get_object(self):
        ti_obj, created = TarjetaProfesional.objects.get_or_create(id=self.kwargs['pk'])
        return ti_obj 

    def get_success_url(self) -> str:
        """ Redirige al dashboard una vez que se completa el formulario """
        return reverse_lazy('listausuario')

# ---------------------------------  CRUD DE USUARIO Perfil Usuario ---------------------------------    

class PerfilUserView(TemplateView):
    template_name = 'registration/perfiluser.html'
    detalle_usuario_list = []
    tarjeta_profesional = None
    telefonos_list = []

    def get(self, request, *args, **kwargs):

        detalle_usuario = DetalleUsuario.objects.filter(usuario = request.user.id)
        tarjeta = TarjetaProfesional.objects.filter(abogado = request.user.id)
        self.tarjeta_profesional = tarjeta[0]
        telefonos = TelefonoUser.objects.filter(usuario = request.user.id)

        for item in detalle_usuario:
            detail = {
                'id' : item.id,
                'fecha_nacimiento': item.fecha_nacimiento,
                'fecha_expedicion': item.fecha_expedicion,
                'estado_civil': item.estado_civil,
                'tipo_documento': item.tipo_documento,
                'genero': item.genero,
                'etnia': item.etnia,
                'vulnerable': item.vulnerable
            }

            if detail not in self.detalle_usuario_list:
                self.detalle_usuario_list.append(detail)

        for phone in telefonos:
            phone_detail = {
                'id': phone.id,
                'tipo_telefono': phone.tipo_telefono,
                'numero': phone.numero_tel,
                'usuario': phone.usuario
            }
            if phone_detail not in self.telefonos_list:
                self.telefonos_list.append(phone_detail)

        return render(request, self.template_name, {'detalle': self.detalle_usuario_list, 
                                                    'tarjeta_profesional': self.tarjeta_profesional, 
                                                    'telefonos':self.telefonos_list})
    

# ---------------------------------  CRUD DE USUARIO Ver Usuario ---------------------------------

class PerfilUserPublicView(DetailView):
    model = Usuario
    template_name = 'registration/perfilpublic.html'

    def get_object(self):
        return get_object_or_404(Usuario, username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        usuario = self.kwargs['username']
        data = get_object_or_404(Usuario, username = usuario)

        if DetalleUsuario.objects.filter(usuario = data.id):
            detalleus = DetalleUsuario.objects.filter(usuario = data.id)
            contexto['detalleus'] = detalleus

        if Group.objects.filter(user= data.id):
            gruposdus = Group.objects.filter(user= data.id)
            contexto['gruposdus'] = gruposdus

        if TelefonoUser.objects.filter(usuario= data.id):
            telefonos = TelefonoUser.objects.filter(usuario= data.id)
            contexto['telefonos'] = telefonos

        if TarjetaProfesional.objects.filter(abogado = data.id):
            tarjetaus = TarjetaProfesional.objects.filter(abogado = data.id)
            contexto['tarjetaus'] = tarjetaus[0]

        contexto['usuario'] = data  

        return contexto        
# ---------------------------------  CRUD DE USUARIO COMPLETO ---------------------------------

# ---------------------------------  Vista Administrativa ---------------------------------
@method_decorator(login_required, name='dispatch')
class DashboardUserView(TemplateView):
    template_name = 'registration/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


