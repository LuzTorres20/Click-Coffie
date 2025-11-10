from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Inventario
from .forms import RegistroUsuarioForm
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import CarritoItem
from .models import Inventario, CarritoItem

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

def ver_carrito(request):
    return render(request, "Paginas/carrito.html")

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Inventario, idProducto=producto_id)

    # Ver si ya existe un registro del mismo producto hoy y que no esté vendido
    item_existente = CarritoItem.objects.filter(
        usuario=request.user,
        producto=producto,
        vendido=False,
        fecha_agregado__date=now().date()
    ).first()

    if item_existente:
        # Incrementar cantidad
        item_existente.cantidad += 1
        item_existente.save()
    else:
        # Crear uno nuevo
        CarritoItem.objects.create(
            usuario=request.user,
            producto=producto,
            cantidad=1
        )

    return redirect("carrito")