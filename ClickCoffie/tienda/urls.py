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
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/modificar/<int:item_id>/<str:accion>/', views.modificar_cantidad, name='modificar_cantidad'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),
    path('carrito/comprar/', views.procesar_compra, name='procesar_compra'),
    path("pago/", views.pago_falso, name="pago_falso"),
    path("procesar/", views.procesar_compra, name="procesar_compra"),
]
