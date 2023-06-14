import os
from django.conf import settings
from django.shortcuts import render
from .models import Contrato, Archivo


def cargaArchivos(request):
    numero_contrato = request.POST.get("contrato", "").upper()
    contrato_encontrado = None
    contrato_encontrado_valido = False

    if numero_contrato:
        try:
            contrato_encontrado = Contrato.objects.get(id_contrato=numero_contrato)
            contrato_encontrado_valido = True
        except Contrato.DoesNotExist:
            contrato_encontrado = None

    if request.method == "POST" and request.FILES.get("archivo"):
        archivo = request.FILES["archivo"]
        descripcion = archivo.name
        tipo = request.POST.get("tipo")
        ruta_archivo = os.path.join(settings.ARCHIVOS_DIR, archivo.name)

        # Guardar el archivo en el directorio de destino
        with open(ruta_archivo, "wb") as f:
            for chunk in archivo.chunks():
                f.write(chunk)

        # Crear una instancia del modelo Archivo y guardar en la base de datos
        archivo_obj = Archivo(
            descripcion=descripcion,
            tipo=tipo,
            contrato=contrato_encontrado,
            ruta_archivo=ruta_archivo,
        )
        archivo_obj.save()

    context = {
        "numero_contrato": numero_contrato,
        "contrato_encontrado": contrato_encontrado,
        "contrato_encontrado_valido": contrato_encontrado_valido,
    }

    return render(request, "modulos/cargaArchivos.html", context)
