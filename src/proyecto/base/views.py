from django.shortcuts import render, redirect
from django.views.generic.list import ListView  # Tipo de página que representa una lista de objetos
from django.views.generic.detail import DetailView # Tipo de página que representa el detalle de un objeto
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView # Permite crear/actualizar/borrar nuevas vistas
from django.contrib.auth.forms import UserCreationForm # Para registrar nuevos usuarios
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin # Establecer los roles de los usaurios y restringir vistas
from django.urls import reverse_lazy # Permite llevar a otra url al ocurrir un evento
from .models import Tarea


# Crear una clase que hereda de LoginView
class Logueo(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True # Determinar si se va a redireccionar o no al usuario logueado

    # Re-escribiremos el método "get_success_url" que define el sitio al cual va el usuario una vez logueado
    def get_success_url(self):
        return reverse_lazy('tareas') # El usuario logueado irá a la página "tareas"


class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')

    # No nos aparezca la funcion de registarnos
    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)

    # Utilizamos esta funcion para que no nos deje redirigirnos a la pagina de registrar
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(PaginaRegistro, self).get(*args, **kwargs)


# Crear una clase que hereda de ListView
class ListaPendientes(LoginRequiredMixin, ListView):
    # Crear un modelo que sea igual a la lista completa
    model = Tarea
    context_object_name = 'tareas'

    # Recuperar la información del usuario en cuestión
    def get_context_data(self, **kwargs): # Argumentos que tengan palabras clave
        context = super().get_context_data(**kwargs) # De esa instancia superior vamos a asegurarnos que ehrede del elemento original
        context['tareas'] = context['tareas'].filter(usuario=self.request.user) # Muestre las tareas del usuario que tenga la sesion iniciada
        context['count'] = context['tareas'].filter(completo=False).count() # Para poder ver las tareas que no esten completas

        valor_buscado = self.request.GET.get('area-buscar') or '' # Va contener nuestro valor buscado
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado # Cuando busqyemos se quede la palabra en el buscador
        return context

# Crear una clase que hereda de DetailView
class DetalleTareas(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'


# Crear una clase que hereda de CreateView
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea  # Se creará un formulario en base a los datos de la clase "Modelo"
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')


    def form_valid(self, form):
        form.instance.usuario = self.request.user # La instancia sea igual al usuario que tenga la sesión iniciada
        return super(CrearTarea, self).form_valid(form)

# Crear una clase que hereda de UpdateView
class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')

# Crear una clase que hereda de DeleteView
class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')



