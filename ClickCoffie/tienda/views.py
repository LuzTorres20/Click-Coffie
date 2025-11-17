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
from django.db.models import F, Sum
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

# Create your views here.

# autentucacion, creacion de usuarios y login
def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get("usuario")
            email = form.cleaned_data.get("email")

            if User.objects.filter(username=username).exists():
                messages.error(request, "El nombre de usuario ya existe, elige otro.")
                return render(request, "formularios/RegistroUsuarios.html", {"form": form})

            if User.objects.filter(email=email).exists():
                messages.error(request, "El correo ya está registrado.")
                return render(request, "formularios/RegistroUsuarios.html", {"form": form})
            

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

@login_required
def ver_carrito(request):
    # Traer los items del carrito del usuario actual que no estén vendidos
    carrito = CarritoItem.objects.filter(usuario=request.user, vendido=False)

    # Calcular el total
    total = carrito.aggregate(total=Sum(F('cantidad') * F('producto__Precio')))['total'] or 0

    context = {
        'carrito': carrito,
        'total': total
    }
    return render(request, "Paginas/carrito.html", context)


@login_required
def agregar_al_carrito(request, producto_id):
    if request.method != "POST":
        return redirect("productos")  # proteger contra GET

    producto = get_object_or_404(Inventario, idProducto=producto_id)
    cantidad = int(request.POST.get("cantidad", 1))

    # Verificar si ya existe el mismo producto no vendido
    item_existente = CarritoItem.objects.filter(
        usuario=request.user,
        producto=producto,
        vendido=False
    ).first()

    if item_existente:
        item_existente.cantidad += cantidad
        item_existente.save()
    else:
        CarritoItem.objects.create(
            usuario=request.user,
            producto=producto,
            cantidad=cantidad
        )

    return redirect("ver_carrito")


@login_required
def carrito(request):
    items = CarritoItem.objects.filter(
        usuario=request.user,
        vendido=False,
        fecha_agregado__date=now().date()
    )
    total = sum(item.subtotal() for item in items)

    return render(request, "carrito.html", {
        "items": items,
        "total": total,
    })


@login_required
def confirmar_compra(request):
    items = CarritoItem.objects.filter(
        usuario=request.user,
        vendido=False,
        fecha_agregado__date=now().date()
    )

    for item in items:
        # Actualizar inventario
        item.producto.stock -= item.cantidad
        item.producto.save()

        # Marcar como vendido
        item.vendido = True
        item.save()

    return redirect("inicio")

@login_required
@require_POST
def modificar_cantidad(request, item_id, accion):
    item = get_object_or_404(CarritoItem, id=item_id, usuario=request.user, vendido=False)

    if accion == 'mas':
        item.cantidad += 1
    elif accion == 'menos' and item.cantidad > 1:
        item.cantidad -= 1

    item.save()
    return redirect('ver_carrito')

def eliminar_item(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, usuario=request.user, vendido=False)
    item.delete()
    return redirect('ver_carrito')  # redirige al carrito

@login_required
def procesar_compra(request):
    # Marcar todos los items del carrito del usuario como vendidos
    carrito = CarritoItem.objects.filter(usuario=request.user, vendido=False)
    for item in carrito:

        producto = item.producto

        if producto.CantidadActual >=item.cantidad:
            producto.CantidadActual -= item.cantidad
        else:
            producto.CantidadActual = 0
        
        producto.save

        item.vendido = True
        item.save()
    
    # Aquí podrías agregar lógica adicional como generar factura, envío, etc.

    return redirect('inicio')  # redirige a la página principal

@login_required
def pasarela_pago(request):
    carrito = CarritoItem.objects.filter(usuario=request.user, vendido=False)
    total = sum(item.cantidad * item.producto.Precio for item in carrito)

    return render(request, "Paginas/pasarela_falsa.html", {"total": total})