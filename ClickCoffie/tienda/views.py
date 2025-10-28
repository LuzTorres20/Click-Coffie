from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib import messages
# Create your views here.

def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request= "El usuario fue registrado correctamente")
            return redirect('Login')
    else:
        form = RegistroUsuarioForm()
    return render(request, "templates/formularios/RegistroUsuarios.html", {"form": form})
    
