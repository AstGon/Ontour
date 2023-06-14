from django.urls import path
from . import views

urlpatterns = [
    # ...
    path("carga_archivos/", views.cargaArchivos, name="carga_archivos"),
    # ...
]
