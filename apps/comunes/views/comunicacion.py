from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from apps.comunes.models import Comunicacion as ComunicacionModel
from apps.comunes.forms.comunicacion import ComunicacionForm


# 
# Comunicacion
#  
class ComunicacionTemplateView(TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return ComunicacionListView.as_view()(request)


class ComunicacionListView(ListView):
    model = ComunicacionModel
    template_name = 'comunes/tabla.html'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = ComunicacionModel.objects.filter(active=True)
        return context
 
 
class ComunicacionCreateView(CreateView):
    model = ComunicacionModel
    form_class = ComunicacionForm
    template_name = 'comunes/formulario.html'
    success_url = reverse_lazy('{app}:list'.format(app=__package__.split('.')[1]))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Tipo de Contacto'
        return context
        
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
 
 
class ComunicacionDetailView(DetailView):
    model = ComunicacionModel
    template_name = 'comunes/detalle.html'
 
 
class ComunicacionUpdateView(UpdateView):
    model = ComunicacionModel
    form_class = ComunicacionForm
    template_name = 'comunes/formulario.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Modificación Tipo de Contacto'
        return context

    def get_success_url(self):
        name = self.model._meta.verbose_name.lower()
        return reverse_lazy('{app}:list'.format(app=name))

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

 
class ComunicacionDeleteView(DeleteView):
    pass
