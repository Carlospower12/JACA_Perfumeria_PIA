from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from sitio import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("perfumes/", views.perfumes, name="perfumes"),
    path(
    "perfume/<str:origen>/<int:identificador>/",
    views.detalle_perfume,
    name="detalle_perfume"
),
    path("contacto/", views.contacto, name="contacto"),
    path("subir/", views.subir_archivo, name="subir_archivo"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
