
from django.urls import path
from .views import CustomLoginView
from . import views

urlpatterns = [
    path("registro/", views.registrar_usuario, name="registro"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("", views.inicio, name= "incio"),
]
