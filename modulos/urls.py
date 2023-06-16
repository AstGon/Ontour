from django.urls import path
from . import views

urlpatterns = [
    path("", views.cargaArchivos, name="cargaArchivos"),
    path("detalles/", views.detalles, name="detalles"),
]
