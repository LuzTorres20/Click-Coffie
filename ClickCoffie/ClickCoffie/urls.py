from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls')),
]

# Servir archivos estáticos (CSS, JS, imágenes de diseño)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    # Servir archivos de media (imágenes subidas por usuarios)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
