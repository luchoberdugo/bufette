from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class DashboardUserView(TemplateView):
    template_name = 'registration/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)