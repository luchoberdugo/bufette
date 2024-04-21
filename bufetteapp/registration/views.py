from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

# Método decorador de login:
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name='dispatch')
class DashboardUserView(TemplateView):
    template_name = 'registration/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)