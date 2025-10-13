from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#formulario para crear usuarios nuevos (estos no tienen acceso a la parte de administrador)
class RegistroUsuarioForm (UserCreationForm):
    usuario = forms.CharField(max_length=50, required=True, label="Usuario")
    nombres = forms.CharField(max_length=50, required=True, label="Nombres")
    apellidos = forms.CharField(max_length=50, required=True, label="Apellidos")
    email = forms.EmailField(required=True, label="Correo Electronico")

    class Meta:
        model = User
        fields = ('usuario', 'nombres', 'apellidos', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['usuario']
        user.first_name = self.cleaned_data['nombres']
        user.last_name = self.cleaned_data['apellidos']
        user.email = self.cleaned_data['email']
        user.is_staff = False
        if commit:
            user.save()
        return user