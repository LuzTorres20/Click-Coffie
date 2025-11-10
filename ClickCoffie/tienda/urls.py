from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView
from . import views

urlpatterns = [
    path("registro/", views.registrar_usuario, name="registro"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("", views.inicio, name="inicio"),  
    path("Productos", views.productos, name="productos"),
]
