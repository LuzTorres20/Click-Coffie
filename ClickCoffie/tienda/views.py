from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Inventario
from .forms import RegistroUsuarioForm
from django.contrib import messages
# Create your views here.

# autentucacion, creacion de usuarios y login
def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El usuario fue registrado correctamente")
            return redirect('/login/')
    else:
        form = RegistroUsuarioForm()
    return render(request, "formularios/RegistroUsuarios.html", {"form": form})
    
class CustomLoginView(LoginView):
    template_name = 'formularios/Login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_staff:
            return '/admin/'
        else:
            return '/'
        

def inicio(request):
    return render(request, "Paginas/inicio.html")

def productos(request):
    productos = Inventario.objects.all() 
    return render(request, "Paginas/productos.html", {'Inventario': productos})