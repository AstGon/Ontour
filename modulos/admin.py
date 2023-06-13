from django.contrib import admin
from .models import Archivo, Ejecutivo, Servicio, TipoArchivo, Contrato, TipoServicio

admin.site.register(Archivo)
admin.site.register(Ejecutivo)
admin.site.register(Servicio)
admin.site.register(TipoArchivo)
admin.site.register(Contrato)
admin.site.register(TipoServicio)
